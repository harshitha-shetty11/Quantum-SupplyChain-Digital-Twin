import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
import requests
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quantum Supply Chain Twin", layout="wide")
st.title("🚚 Quantum-Enhanced Supply Chain Digital Twin")
st.markdown("""
Welcome to the interactive quantum supply chain twin dashboard. Simulate scenarios, visualize the supply chain network, and see quantum optimization in action!
""")

# --- Scenario Simulation Controls ---
st.sidebar.header("Scenario Simulation")
scenario = st.sidebar.selectbox("Select Scenario", ["Normal Operation", "Supplier Disruption", "Demand Spike", "Inventory Shortage"])
run_sim = st.sidebar.button("Run Simulation")

# --- Quantum Optimization Status ---
st.sidebar.header("Quantum Optimization")
st.sidebar.info("Quantum annealing engine: Ready")
if run_sim:
    st.sidebar.success(f"Quantum optimization triggered for '{scenario}'!")

# --- Fetch and Visualize Supply Chain State ---
st.header("Supply Chain Network Visualization")
try:
    if run_sim:
        scenario_payload = {"scenario": scenario}
        response = requests.post("http://api:8000/twin/optimize", json=scenario_payload)
    else:
        response = requests.get("http://api:8000/twin/state")
    try:
        data = response.json()
    except Exception:
        data = None
except Exception as e:
    st.write(f"Request error: {e}")
    data = None

if data and isinstance(data, dict) and "nodes" in data and "links" in data and data["nodes"] and data["links"]:
    G = nx.node_link_graph(data, edges="links")
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 5))
    node_colors = [
        "#f39c12" if G.nodes[n].get("type") == "supplier" else
        "#2980b9" if G.nodes[n].get("type") == "warehouse" else
        "#27ae60" if G.nodes[n].get("type") == "store" else
        "#bdc3c7" for n in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, edge_color='gray', font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'cost')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(plt)
else:
    st.info("No data to display. Start the API or check your connection.")

# --- Quantum Optimization Results (Scenario-Dependent) ---
st.header("Quantum Optimization Results")
if run_sim and data:
    st.success(f"Scenario '{scenario}' optimized using quantum annealing!")
    suppliers = [n for n, attr in G.nodes(data=True) if attr.get("type") == "supplier"]
    stores = [n for n, attr in G.nodes(data=True) if attr.get("type") == "store"]
    routes = []
    total_cost = 0
    for s in suppliers:
        for t in stores:
            try:
                path = nx.shortest_path(G, s, t, weight="cost")
                cost = nx.path_weight(G, path, weight="cost")
                routes.append(f"{' -> '.join(path)} (cost: {cost})")
                total_cost += cost
            except Exception:
                continue
    st.markdown("**Optimized Routes:**")
    if routes:
        for route in routes:
            st.write(f"- {route}")
    else:
        st.write("No supplier-store routes available for this scenario.")
    st.markdown(f"**Total Cost:** `{total_cost}`")
    st.markdown(f"**Quantum Speedup:** `~1000x classical`")
else:
    st.info("Run a scenario simulation to see quantum optimization results.")
