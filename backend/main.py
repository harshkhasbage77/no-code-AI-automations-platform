from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://react-flow-graphs-frontend.vercel.app"],  # Frontend origin & # Deployed frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class Node(BaseModel):
    id: str

class Edge(BaseModel):
    source: str
    target: str

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post("/pipelines/parse")
async def parse_pipeline(pipeline: Pipeline):
    nodes = pipeline.nodes
    edges = pipeline.edges

    # Calculate number of nodes and edges
    num_nodes = len(nodes)
    num_edges = len(edges)

    # Build adjacency list
    adjacency_list = {node.id: [] for node in nodes}
    for edge in edges:
        adjacency_list[edge.source].append(edge.target)

    # Check if the graph is a Directed Acyclic Graph (DAG)
    def is_dag():
        visited = set()
        stack = set()

        def visit(node):
            if node in stack:  # Cycle detected
                return False
            if node in visited:  # Already processed
                return True
            stack.add(node)
            for neighbor in adjacency_list[node]:
                if not visit(neighbor):
                    return False
            stack.remove(node)
            visited.add(node)
            return True

        return all(visit(node.id) for node in nodes)

    is_dag_result = is_dag()

    # Return the results
    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "is_dag": is_dag_result
    }
