# LangGraph Project Flow Diagram

```mermaid
graph TD
    A[SRS Upload(.docx)]-->B[Analyze the SRS (Groq)]
    B-->C[Generate FastAPI Project (structure)]
    C-->D[Generate Tests from Business Rules]
    D-->E[Generate Code to pass test cases]
    E-->F[ZIP Project]
    F-->G[Generate Documentation + Diagram]
    G-->H[Final Output as ZIP]
        
```