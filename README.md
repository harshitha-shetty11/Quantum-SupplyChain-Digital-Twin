# Quantum Supply Chain Twin

This project is a digital twin for a supply chain. You can simulate supplier disruptions, demand spikes, and inventory issues, and see how the network responds. The dashboard helps you visualize the supply chain and optimization results.

## How to Run
1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the backend API:
   ```bash
   uvicorn src.api.main:app --reload
   ```
3. Start the dashboard:
   ```bash
   streamlit run src/visualization/dashboard/main_dashboard.py
   ```

## Main Features
- Simulate different supply chain scenarios
- Visualize the network and results
- Try quantum-inspired optimization (optional)

## Notes
- For quantum tasks, see the AWS Braket setup in `deployment/aws/braket_setup.py`.
- You can run locally or with Docker/Kubernetes (see deployment folder).

---

Feel free to use, modify, or extend this project for your own supply chain experiments.
