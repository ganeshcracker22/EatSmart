// EatSmart Risk AI - Frontend Logic (Stitch UI Edition)

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const scanBtn = document.getElementById('scan-food-btn');
    const foodInput = document.getElementById('food-input-field');
    
    // Result Elements
    const riskIndexVal = document.getElementById('risk-index-value');
    const aiInsightText = document.getElementById('ai-insight-text');
    const recoveryVal = document.getElementById('recovery-val');
    const recoveryBar = document.getElementById('recovery-bar');

    const runAnalysis = async (foodName) => {
        if (!foodName) {
            alert("Please input a food sample to scan.");
            return;
        }
        
        // Show Loading State
        scanBtn.classList.add('animate-spin');
        scanBtn.querySelector('span').innerText = 'sync';
        aiInsightText.innerText = "Accessing molecular database...";
        
        try {
            // Simulated network delay
            await new Promise(r => setTimeout(r, 1500));
            
            const response = await fetch('http://localhost:8000/analyze-food', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    food_name: foodName,
                    user_goal: "muscle gain"
                })
            });

            if (!response.ok) throw new Error('API Error');

            const data = await response.json();
            updateUI(data);
            
        } catch (error) {
            console.error(error);
            aiInsightText.innerText = "Connection lost. Ensure NutriTwin Backend is online.";
        } finally {
            scanBtn.classList.remove('animate-spin');
            scanBtn.querySelector('span').innerText = 'center_focus_strong';
        }
    };

    const updateUI = (data) => {
        // Update Risk Index with animation feel
        riskIndexVal.innerText = `${data.risk_score}.0%`;
        
        // Update Recovery Level (derived from protein/muscle support)
        const recoverScore = data.simulation.muscle_support === 'high' ? 92 : (data.simulation.muscle_support === 'medium' ? 75 : 45);
        recoveryVal.innerText = recoverScore;
        recoveryBar.style.width = `${recoverScore}%`;
        
        // Update AI Insight with recommendation + consequence
        aiInsightText.innerText = `"${data.recommendation.suggested_alternative.toUpperCase()} suggested. ${data.consequences.immediate_effect}"`;
        
        // Style adjustments based on risk
        const riskColor = data.risk_score > 60 ? '#ff7166' : '#9cff93';
        riskIndexVal.style.color = riskColor;
        
        console.log("Stitch UI Analysis Complete:", data);
    };

    // Event Listeners
    scanBtn.addEventListener('click', () => runAnalysis(foodInput.value));
    
    foodInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') runAnalysis(foodInput.value);
    });
});
