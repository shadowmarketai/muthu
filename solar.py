import streamlit as st
import subprocess
import sys
import os

def main():
    st.set_page_config(page_title="Solar Power Calculator", page_icon="☀️")
    st.title("☀️ Solar Power Savings Calculator")

    st.markdown("""
    Calculate how much you can save by installing solar panels on your roof.
    Enter your details below:
    """)

    # Inputs
    location = st.selectbox("Select your location (for average sun hours):", [
        "Tropical (5-6 hours/day)",
        "Temperate (3-4 hours/day)",
        "Cold (2-3 hours/day)"
    ])

    sun_hours = 5.5 if location == "Tropical (5-6 hours/day)" else 3.5 if location == "Temperate (3-4 hours/day)" else 2.5

    roof_area = st.number_input("Roof area available (in sq. meters):", min_value=10.0, max_value=1000.0, value=100.0)
    panel_efficiency = st.slider("Panel efficiency (%):", min_value=10, max_value=25, value=18)
    electricity_cost = st.number_input("Electricity cost (₹ per kWh):", min_value=1.0, value=8.0)
    system_cost_per_kw = st.number_input("Installed system cost (₹ per kW):", min_value=30000.0, value=50000.0)
    budget = st.number_input("Your budget for solar (₹):", min_value=50000.0, value=200000.0)

    # Constants
    panel_power_density = 0.15  # kW per m² (average)

    # Calculate button
    if st.button("Calculate"):
        try:
            # Calculations
            max_system_size_kw = roof_area * panel_power_density * (panel_efficiency / 18)
            max_cost = max_system_size_kw * system_cost_per_kw

            system_size_kw = min(budget / system_cost_per_kw, max_system_size_kw)

            annual_energy_kwh = system_size_kw * sun_hours * 365
            annual_savings = annual_energy_kwh * electricity_cost
            payback_period = (system_cost_per_kw * system_size_kw) / annual_savings
            co2_saved_per_year = annual_energy_kwh * 0.92  # kg CO2 per kWh

            # Output
            st.success(f"Estimated system size: **{system_size_kw:.2f} kW**")
            st.info(f"Annual energy production: **{annual_energy_kwh:.0f} kWh**")
            st.info(f"Estimated annual savings: **₹{annual_savings:,.0f}**")
            st.warning(f"Payback period: **{payback_period:.1f} years**")
            st.success(f"CO₂ avoided per year: **{co2_saved_per_year/1000:.1f} tons**")

            st.markdown("---")
            st.markdown("### 📈 Insights:")
            if payback_period < 5:
                st.write("✅ Great investment! You'll recover your cost quickly.")
            elif payback_period < 10:
                st.write("☑️ Decent investment. Consider if electricity rates are rising.")
            else:
                st.write("⚠️ Long payback period. Evaluate subsidies or wait for lower prices.")
        except Exception as e:
            st.error(f"An error occurred during calculation: {e}")

if __name__ == "__main__":
    # Auto-launch Streamlit if run with python
    if "streamlit" not in sys.argv[0]:
        print("ℹ️ Relaunching with Streamlit...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)])
    else:
        main()
