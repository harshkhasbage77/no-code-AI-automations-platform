# No-code AI Automation Platform

This project is a no-code platform for creating and managing AI-driven automation pipelines. It consists of a backend built with FastAPI and a frontend built with React.

Demo: [Click Here](https://react-flow-graphs-frontend.vercel.app/)

Link: https://react-flow-graphs-frontend.vercel.app/

Backend: https://no-code-ai-automations-platform-backend.onrender.com/


## Project Structure

### Backend

The backend is built with FastAPI and provides APIs for managing pipelines. It includes the following key components:

- **main.py**: The main entry point of the backend application.
- **Node, Edge, Pipeline**: Pydantic models representing the structure of a pipeline.

#### Running the Backend

1. Create a virtual environment:
    ```sh
    python -m venv .myenv
    ```

2. Activate the virtual environment:
    ```sh
    source .myenv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

The backend server will be available at `http://127.0.0.1:8000`.

### Frontend

The frontend is built with React and provides a drag-and-drop interface for creating pipelines. It includes the following key components:

- **App.js**: The main entry point of the frontend application.
- **PipelineToolbar**: A toolbar for adding nodes to the pipeline.
- **PipelineUI**: The main UI for displaying and managing the pipeline.
- **SubmitButton**: A button for submitting the pipeline to the backend.

#### Running the Frontend

1. Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

3. Start the development server:
    ```sh
    npm start
    ```

The frontend application will be available at `http://localhost:3000`.

### API Endpoints

#### `POST /pipelines/parse`

Parses a pipeline and returns the number of nodes, number of edges, and whether the graph is a Directed Acyclic Graph (DAG).

