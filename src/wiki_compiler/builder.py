import os
import re
import yaml
import json
import networkx as nx
from networkx.readwrite import json_graph
from pathlib import Path
from .contracts import KnowledgeNode

TRANSCLUSION_REGEX = re.compile(r'!\[\[(.*?)\]\]')
FRONTMATTER_REGEX = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def build_wiki(source_dir: Path, dest_dir: Path, graph_path: Path):
    os.makedirs(dest_dir, exist_ok=True)
    
    # Start NetworkX Directional Graph
    G = nx.DiGraph()
    files_index = {}

    # Step 1: Indexing
    for filepath in source_dir.rglob("*.md"):
        files_index[filepath.stem] = filepath

    # Step 2: Build Nodes and Edges
    for filepath in source_dir.rglob("*.md"):
        content = filepath.read_text(encoding="utf-8")
        
        yaml_match = FRONTMATTER_REGEX.search(content)
        raw_markdown = content
        
        if yaml_match:
            yaml_str = yaml_match.group(1)
            raw_markdown = content[yaml_match.end():]
            try:
                node_data = yaml.safe_load(yaml_str)
                validated_node = KnowledgeNode(**node_data)
                
                # 1. Add NODE to NetworkX
                node_id = validated_node.identity.node_id
                G.add_node(
                    node_id, 
                    type=validated_node.identity.node_type,
                    status=validated_node.compliance.status if validated_node.compliance else "unknown",
                    # Save complete JSON in node metadata
                    schema=validated_node.model_dump() 
                )
                
                # 2. Add EDGES to NetworkX
                for edge in validated_node.edges:
                    G.add_edge(
                        node_id, 
                        edge.target_id, 
                        relation=edge.relation_type,
                        metadata=edge.metadata
                    )
                    
            except Exception as e:
                print(f"[⚠️] Ignoring invalid metadata in {filepath}: {e}")

        # Render Markdown (Baking transclusions)
        def replace_transclusion(match):
            target_name = match.group(1)
            if target_name in files_index:
                target_path = files_index[target_name]
                rel_path = os.path.relpath(target_path, filepath.parent)
                return f"**[🔗 See {target_name}]({rel_path})**"
            return f"*[⚠️ Broken transclusion: {target_name}]*"

        compiled_markdown = TRANSCLUSION_REGEX.sub(replace_transclusion, raw_markdown)
        
        rel_dest = filepath.relative_to(source_dir)
        dest_filepath = dest_dir / rel_dest
        os.makedirs(dest_filepath.parent, exist_ok=True)
        dest_filepath.write_text(compiled_markdown, encoding="utf-8")

    # Step 3: Export Graph to JSON
    data = json_graph.node_link_data(G)
    graph_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    
    print(f"[📊] Graph generated: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.")
