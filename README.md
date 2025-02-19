# Project Structure Visualization

```mermaid
graph TD;
    subgraph Main
        A[Startup Event] --> B[Shutdown Event]
        B --> C[Health Check API]
        C --> D[Filter Releases API]
        D --> E[Get Test File API]
    end
    
    subgraph Endpoints
        F[Discord Send API] --> G[Testfile Get API]
        G --> H[Organization Post API]
        H --> I[Folder Post API]
        I --> J[APK Post API]
        J --> K[APK Version Upload API]
        K --> L[APIs Post API]
        L --> M[Testplan Org API]
        M --> N[Admin Test Plans Analysis API]
        N --> O[GitHub Installation Init API]
        O --> P[Slack Authorize API]
        P --> Q[Report Post API]
        Q --> R[Project Post API]
    end

    subgraph RelatedAPIs
        S[Testfile Folder Get API] --> T[Testfile ID Get API]
        T --> U[Testfile Post API]
        U --> V[Testfile Patch API]
        V --> W[Testfile Delete API]
        X[Organization ID Get API] --> Y[Organization List Get API]
        Y --> Z[Organization Patch API]
        Z --> AA[Organization Delete API]
        AB[Folder ID Get API] --> AC[Folder Project Get API]
        AC --> AD[Folder Patch API]
        AD --> AE[Folder Delete API]
        AF[APK Organization Get API] --> AG[APK ID Get API]
        AG --> AH[APK Patch API]
        AH --> AI[APK Delete API]
        AJ[APK Version Releases Get API] --> AK[APK Version Filter Post API]
        AL[APIs List Get API] --> AM[APIs ID Get API]
        AM --> AN[APIs Patch API]
        AN --> AO[APIs Delete API]
        AP[Testplan ID Get API] --> AQ[Testplan Post API]
        AQ --> AR[Testplan Patch API]
        AR --> AS[Testplan Delete API]
        AT[Testplan Status Get API] --> AU[Testplan Status Run Get API]
        AU --> AV[Testplan Status Patch API]
        AV --> AW[Testplan Status Post API]
        AX[Admin Test Plans Get API] --> AY[Admin Test Plans Test Files Get API]
        AY --> AZ[Admin Test Plans Test File ID Get API]
        AZ --> BA[Admin Test Files ID Get API]
        BB[GitHub Installation Status Get API] --> BC[GitHub Webhooks Post API]
        BC --> BD[GitHub Create Repo Post API]
        BD --> BE[GitHub Push Code Post API]
        BE --> BF[GitHub Integration Get API]
        BF --> BG[GitHub Integration Delete API]
        BH[GitHub Repositories Get API] --> BI[GitHub Sync Post API]
        BJ[Slack OAuth Callback Get API] --> BK[Slack Channels Get API]
        BK --> BL[Slack Workspaces Get API]
        BL --> BM[Slack Channels Messages Post API]
        BM --> BN[Slack Workspaces Delete API]
        BO[Report Logs Post API] --> BP[Report ID Get API]
        BP --> BQ[Report Patch API]
        BQ --> BR[Report Generate Post API]
        BR --> BS[Report Send Discord Post API]
        BS --> BT[Report Check Approval Get API]
        BU[Project List Get API] --> BV[Project Patch API]
        BV --> BW[Project Archive Put API]
        BW --> BX[Project ID Get API]
        BX --> BY[Project Delete API]
    end

    Endpoints --> RelatedAPIs
```


This updated diagram includes the related APIs, expanding the structure to show the connections and relationships between various endpoints within the project. Each node represents an API, and the arrows indicate the flow or relationship between them.

[View README2](README2.md)
