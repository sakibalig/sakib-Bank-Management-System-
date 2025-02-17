# 🌍 Flowchart Visualization with Mermaid

This diagram represents interconnected relationships with cycles, showing dependencies between different entities.

```mermaid
graph TD;
  %% 🌳 Cycle 1: Apple → Human → Tree → Soil → Apple
  A["🍏 Apple"] -->|Eaten by| B["👨 Human"];
  B -->|Eats| A;

  B -->|Plants| C["🌲 Tree"];
  C -->|Planted by| B;

  C -->|Grows in| D["🌱 Soil"];
  D -->|Nourishes| C;

  D -->|Supports growth of| A;
  A -->|Receives nutrients from| D;

  %% ☀️ Cycle 2: Sun → Plant → Oxygen → Human → Sun
  E["☀️ Sun"] -->|Provides sunlight| F["🌿 Plant"];
  F -->|Uses sunlight| E;

  F -->|Releases| G["💨 Oxygen"];
  G -->|Produced by| F;

  G -->|Inhaled by| H["👨 Human"];
  H -->|Breathes| G;

  H -->|Needs energy from| E;
  E -->|Provides warmth| H;

  %% 🌊 Cycle 3: Water → Fish → Bird → Cloud → Rain → Water
  I["💧 Water"] -->|Habitat for| J["🐟 Fish"];
  J -->|Lives in| I;

  J -->|Eaten by| K["🐦 Bird"];
  K -->|Preys on| J;

  K -->|Flies near| L["☁️ Cloud"];
  L -->|Provides shade to| K;

  L -->|Turns into| M["🌧️ Rain"];
  M -->|Forms from| L;

  M -->|Refills| I;
  I -->|Receives from| M;

  %% 🚗 Cycle 4: Car → Fuel → Factory → Air Pollution → Human → Car
  N["🚗 Car"] -->|Runs on| O["⛽ Fuel"];
  O -->|Used in| N;

  O -->|Processed at| P["🏭 Factory"];
  P -->|Produces| O;

  P -->|Emits| Q["🌫️ Air Pollution"];
  Q -->|Caused by| P;

  Q -->|Affects| R["👨 Human"];
  R -->|Suffers from| Q;

  R -->|Drives| N;
  N -->|Used by| R;

  %% 🎓 Cycle 5: Teacher → Student → Knowledge → Books → Teacher
  S["🎓 Teacher"] -->|Teaches| T["🧑‍🎓 Student"];
  T -->|Learns from| S;

  T -->|Acquires| U["📚 Knowledge"];
  U -->|Gained by| T;

  U -->|Stored in| V["📖 Books"];
  V -->|Contains| U;

  V -->|Used by| S;
  S -->|Reads| V;

  %% 💻 Cycle 6: Computer → User → Internet → Data → Computer
  W["💻 Computer"] -->|Used by| X["👤 User"];
  X -->|Operates| W;

  X -->|Accesses| Y["🌐 Internet"];
  Y -->|Browsed by| X;

  Y -->|Stores| Z["📊 Data"];
  Z -->|Processed by| Y;

  Z -->|Stored on| W;
  W -->|Analyzes| Z;
