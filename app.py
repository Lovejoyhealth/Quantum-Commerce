    
from flask import Flask, request, jsonify
from emotion import derive_emotion
from strategy import recommend_strategy

app = Flask(__name__)

# About page route (must be after app = Flask(__name__))
@app.route('/about')
def about():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quantum Cognitive Commerce: The Future of Personalization</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0a0a0a;
            color: #e2e8f0;
        }
        .hero-gradient {
            background: radial-gradient(circle at 50% 30%, rgba(56, 189, 248, 0.15), transparent 50%);
        }
        .section-gradient {
             background: radial-gradient(circle at 50% 0%, rgba(192, 132, 252, 0.1), transparent 60%);
        }
        .card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }
        .tag {
            background-color: rgba(56, 189, 248, 0.1);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
        .math-symbol {
            font-family: 'Times New Roman', serif;
            font-style: italic;
            font-size: 1.25rem;
            color: #c084fc;
        }
        .workflow-arrow {
            position: relative;
        }
        .workflow-arrow::after {
            content: '→';
            position: absolute;
            right: -2rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 2rem;
            color: #38bdf8;
            opacity: 0.5;
        }
        @media (max-width: 1023px) {
            .workflow-arrow::after {
                content: '↓';
                right: 50%;
                transform: translateX(50%);
                top: 100%;
                margin-top: 1rem;
            }
        }
    </style>
</head>
<body class="antialiased">

    <!-- Hero Section -->
    <div class="relative min-h-screen flex items-center justify-center p-4 overflow-hidden hero-gradient">
        <div class="absolute inset-0 flex items-center justify-center opacity-20">
            <img src="http://googleusercontent.com/file_content/1" alt="Quantum Brain Artifact" class="max-w-3xl w-full h-auto" />
        </div>
        <div class="text-center z-10">
            <span class="tag text-sm font-medium px-3 py-1 rounded-full">Next-Generation AI</span>
            <h1 class="text-4xl md:text-6xl font-black mt-4 text-white">Quantum Cognitive Commerce</h1>
            <p class="mt-4 max-w-2xl mx-auto text-lg md:text-xl text-slate-300">
                Moving beyond classical AI to understand the emotional and cognitive drivers of choice. We model the ambiguity of human decisions to connect people with their ultimate purchasing journey.
            </p>
            <div class="mt-8 flex justify-center gap-4">
                <a href="#concepts" class="bg-sky-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-sky-600 transition-all">Explore the Concepts</a>
                <a href="#usecase" class="bg-slate-700 text-white font-bold py-3 px-6 rounded-lg hover:bg-slate-600 transition-all">See the Use Case</a>
            </div>
        </div>
    </div>

    <!-- Introduction to Quantum Cognitive Modeling -->
    <section id="concepts" class="py-20 px-4 section-gradient">
        <div class="max-w-5xl mx-auto">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-white">Why Quantum Cognition?</h2>
                <p class="mt-4 text-lg text-slate-400 max-w-3xl mx-auto">Classical models assume we are rational calculators. Quantum cognitive models embrace the reality: human decision-making is ambiguous, contextual, and deeply influenced by emotion. We don't just *have* preferences; we construct them in the moment.</p>
            </div>

            <div class="grid md:grid-cols-2 gap-8 items-start">
                <!-- Superposition Card -->
                <div class="card p-8 rounded-2xl">
                    <h3 class="text-2xl font-bold text-white">1. Superposition: The State of Indecision</h3>
                    <p class="mt-4 text-slate-300">Before making a choice, your mind holds multiple options at once. This state includes not only your preferences but also your current emotional state (e.g., calm, excited, stressed), which colors your perception of the choices.</p>
                    <div class="mt-6 p-6 bg-black rounded-lg text-center">
                        <div class="text-2xl font-mono text-slate-200 flex items-center justify-center space-x-2">
                            <span class="math-symbol">|ψ⟩</span>
                            <span>=</span>
                            <span class="math-symbol">|Emotion⟩</span>
                            <span class="text-xl">⊗</span>
                            <span class="text-xl">(</span>
                            <span class="math-symbol">α</span>
                            <span class="math-symbol">|Choice A⟩</span>
                            <span>+</span>
                            <span class="math-symbol">β</span>
                            <span class="math-symbol">|Choice B⟩</span>
                            <span class="text-xl">)</span>
                        </div>
                        <p class="mt-4 text-sm text-slate-400">Your total cognitive state <span class="math-symbol">|ψ⟩</span> is an entanglement of your emotional state and your potential choices.</p>
                    </div>
                </div>

                <!-- Contextuality Card -->
                <div class="card p-8 rounded-2xl">
                    <h3 class="text-2xl font-bold text-white">2. Contextuality: Order Matters</h3>
                    <p class="mt-4 text-slate-300">The order in which you receive information fundamentally changes your final decision. Seeing a high price when you're feeling stressed has a different impact than seeing it when you're calm. The interaction of context and emotion shapes the outcome.</p>
                    <div class="mt-6 p-6 bg-black rounded-lg">
                        <p class="text-center font-mono text-lg text-slate-200">Context A, then B <span class="text-red-500 font-bold text-2xl">≠</span> Context B, then A</p>
                        <div class="mt-4 flex justify-center items-center space-x-4">
                            <div class="text-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto text-sky-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" /></svg>
                                <p class="mt-2 text-sm text-slate-300">Path 1</p>
                            </div>
                            <div class="text-red-500 font-bold text-2xl">...</div>
                             <div class="text-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                <p class="mt-2 text-sm text-slate-300">Different Outcome</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Use Case Section -->
    <section id="usecase" class="py-20 px-4">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-white">Use Case: Emotion-Aware E-Commerce</h2>
                <p class="mt-4 text-lg text-slate-400 max-w-3xl mx-auto">We use this new understanding of decision-making to create a recommendation engine for e-commerce platforms that respects privacy while connecting customers to products they truly want.</p>
            </div>

            <!-- Workflow Diagram -->
            <div class="grid lg:grid-cols-3 gap-8 md:gap-16 text-center">
                <!-- Step 1 -->
                <div class="workflow-arrow">
                    <div class="card p-6 rounded-2xl h-full flex flex-col items-center justify-center">
                        <div class="bg-sky-500/20 p-3 rounded-full mb-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-sky-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                        </div>
                        <h4 class="font-bold text-xl text-white">1. Federated State Prep</h4>
                        <p class="text-slate-400 mt-2 text-sm">On the user's device, consented bioinformatics data is used to create an initial "Cognitive State Vector," representing latent preferences and current emotional state. <strong class="text-sky-400">Raw data never leaves the device.</strong></p>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="workflow-arrow">
                    <div class="card p-6 rounded-2xl h-full flex flex-col items-center justify-center">
                        <div class="bg-purple-500/20 p-3 rounded-full mb-4">
                           <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 21h7a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v11m0 5l4.879-4.879m0 0a3 3 0 104.243-4.242 3 3 0 00-4.243 4.242z" /></svg>
                        </div>
                        <h4 class="font-bold text-xl text-white">2. Cognitive Simulation</h4>
                        <p class="text-slate-400 mt-2 text-sm">The anonymized state vector and browsing context are sent to the cloud. A quantum cognitive model simulates how the user's emotional state interacts with the product, predicting the most likely choices.</p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="">
                    <div class="card p-6 rounded-2xl h-full flex flex-col items-center justify-center">
                        <div class="bg-emerald-500/20 p-3 rounded-full mb-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                        </div>
                        <h4 class="font-bold text-xl text-white">3. Hyper-Personalization</h4>
                        <p class="text-slate-400 mt-2 text-sm">The simulation results are sent back, and the e-commerce store dynamically updates. The user sees products that resonate with their cognitive and emotional state, increasing engagement and sales.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-4 border-t border-slate-800">
        <div class="max-w-5xl mx-auto text-center">
            <p class="text-slate-400">Exploring the intersection of quantum theory, cognitive science, and artificial intelligence.</p>
            <p class="text-sm text-slate-500 mt-2">Conceptual Website &copy; 2025</p>
        </div>
    </footer>

</body>
</html>
'''
from flask import Flask, request, jsonify
from emotion import derive_emotion
from strategy import recommend_strategy

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PoC: Emotion-Aware Cognitive Recommender</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0a0a0a;
            color: #e2e8f0;
        }
        .card {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }
        .product-card {
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        .product-card.selected {
            border-color: #38bdf8;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
            transform: scale(1.03);
        }
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            background: #38bdf8;
            cursor: pointer;
            border-radius: 50%;
        }
        input[type="range"]::-moz-range-thumb {
            width: 20px;
            height: 20px;
            background: #38bdf8;
            cursor: pointer;
            border-radius: 50%;
        }
        .recommendation-item {
            transition: all 0.3s ease-in-out;
        }
        .math-symbol {
            font-family: 'Times New Roman', serif;
            font-style: italic;
            font-size: 1.1rem;
            color: #c084fc;
        }
        .derived-bar-bg {
            background-color: #374151;
        }
        .derived-bar-fill {
            background-color: #a78bfa;
            transition: width 0.3s ease-in-out;
        }
    </style>
</head>
<body class="antialiased">

    <div class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">
        <!-- Header -->
        <div class="text-center my-8 relative">
             <img src="http://googleusercontent.com/file_content/1" alt="Quantum Brain Artifact" class="max-w-md w-full h-auto mx-auto opacity-20" />
            <div class="absolute inset-0 flex flex-col items-center justify-center">
                <h1 class="text-4xl font-bold text-white">Emotion-Aware Recommender</h1>
                <p class="mt-2 text-lg text-slate-400">A PoC simulating how emotion and context shape preference.</p>
            </div>
        </div>

        <div class="grid lg:grid-cols-3 gap-8">
            <!-- Left Column: Controls and Profile -->
            <div class="lg:col-span-1 space-y-8">
                <div class="card p-6 rounded-lg">
                    <h2 class="text-2xl font-bold text-white border-b border-slate-600 pb-3">1. Simulated Cognitive State</h2>
                    <p class="text-sm text-slate-400 mt-3">Define the customer's latent traits and biometric data.</p>
                    
                    <h3 class="font-semibold text-lg text-sky-400 mt-6">Cognitive Traits</h3>
                    <div id="cognitive-profile" class="mt-4 space-y-4"></div>
                    
                    <h3 class="font-semibold text-lg text-green-400 mt-8">Fusion Sensor Data (Biometrics)</h3>
                    <div id="biometric-inputs" class="mt-4 space-y-4"></div>

                    <h3 class="font-semibold text-lg text-purple-400 mt-8">Derived Emotional State</h3>
                    <div id="emotional-profile" class="mt-4 space-y-4"></div>
                </div>
            </div>

            <!-- Right Column: Products and Recommendations -->
            <div class="lg:col-span-2 space-y-8">
                <div class="card p-6 rounded-lg">
                    <h2 class="text-2xl font-bold text-white border-b border-slate-600 pb-3">2. Product Catalog</h2>
                    <p class="text-sm text-slate-400 mt-3">Click on a product to simulate viewing it. Observe how this "context" changes the recommendations below.</p>
                    <div id="product-catalog" class="mt-6 grid grid-cols-2 md:grid-cols-3 gap-4"></div>
                </div>
                <div class="card p-6 rounded-lg">
                    <h2 class="text-2xl font-bold text-white border-b border-slate-600 pb-3">3. Real-Time Recommendations</h2>
                     <p class="text-sm text-slate-400 mt-3">Products are ranked by their alignment with your current cognitive & emotional state.</p>
                    <div id="recommendations" class="mt-6 space-y-3"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // --- DATA DEFINITIONS ---
            const COGNITIVE_TRAITS = {
                'Novelty Seeking': 'Values new and unique items.',
                'Quality Focus': 'Prioritizes craftsmanship and durability.',
                'Price Sensitivity': 'Influenced by lower prices (inverted).',
            };
            
            const BIOMETRIC_INPUTS = {
                'Heart Rate Variability (HRV)': 'High HRV suggests calm; low suggests stress.',
                'Electrodermal Activity (EDA)': 'Low EDA suggests calm; high suggests arousal/stress.',
                'Brainwave Ratio (Alpha/Beta)': 'High ratio suggests focus; low suggests distraction.'
            };

            const EMOTIONAL_STATES = {
                'Calm vs. Stressed': 'Derived from HRV and EDA.',
                'Focused vs. Distracted': 'Derived from Brainwave Ratio.',
            };

            const PRODUCTS = [
                { id: 1, name: 'Cozy Cashmere Throw', emoji: '🧣', traits: { 'Novelty Seeking': 0.2, 'Quality Focus': 0.9, 'Price Sensitivity': 0.3 }, emotion: { 'Calm vs. Stressed': 0.1, 'Focused vs. Distracted': 0.4 } },
                { id: 2, name: 'High-Tech Drone', emoji: '🚁', traits: { 'Novelty Seeking': 0.9, 'Quality Focus': 0.7, 'Price Sensitivity': 0.2 }, emotion: { 'Calm vs. Stressed': 0.8, 'Focused vs. Distracted': 0.9 } },
                { id: 3, name: 'Meditation App Sub', emoji: '🧘', traits: { 'Novelty Seeking': 0.5, 'Quality Focus': 0.4, 'Price Sensitivity': 0.8 }, emotion: { 'Calm vs. Stressed': 0.2, 'Focused vs. Distracted': 0.8 } },
                { id: 4, name: 'Minimalist Desk Organizer', emoji: '🗂️', traits: { 'Novelty Seeking': 0.3, 'Quality Focus': 0.8, 'Price Sensitivity': 0.6 }, emotion: { 'Calm vs. Stressed': 0.4, 'Focused vs. Distracted': 1.0 } },
                { id: 5, name: 'Impulse-Buy Gadget', emoji: '🕹️', traits: { 'Novelty Seeking': 0.8, 'Quality Focus': 0.2, 'Price Sensitivity': 0.9 }, emotion: { 'Calm vs. Stressed': 0.9, 'Focused vs. Distracted': 0.2 } },
                { id: 6, name: 'Luxury Fountain Pen', emoji: '✒️', traits: { 'Novelty Seeking': 0.6, 'Quality Focus': 1.0, 'Price Sensitivity': 0.1 }, emotion: { 'Calm vs. Stressed': 0.3, 'Focused vs. Distracted': 0.7 } }
            ];

            // --- STATE MANAGEMENT ---
            let cognitiveState = {};
            let biometricState = {};
            let emotionalState = {};
            let selectedProductId = null;
            const COGNITIVE_WEIGHT = 0.6;
            const EMOTIONAL_WEIGHT = 0.4;

            // --- CORE LOGIC ---
            function normalize(vector) {
                const mag = Math.sqrt(vector.reduce((sum, val) => sum + val * val, 0));
                return mag === 0 ? vector : vector.map(v => v / mag);
            }

            function dotProduct(vecA, vecB) {
                return vecA.reduce((sum, val, i) => sum + val * vecB[i], 0);
            }

            function projectState(currentStateVec, contextVec, strength = 0.5) {
                const projected = currentStateVec.map((v, i) => v * (1 - strength) + contextVec[i] * strength);
                return normalize(projected);
            }

            const getVector = (stateObj, keys) => normalize(keys.map(key => stateObj[key]));
            const getProductVector = (product, keys) => normalize(keys.map(key => product[key]));

            // *** SENSOR FUSION LOGIC ***
            function deriveEmotionalState() {
                // Rule for 'Calm vs. Stressed'
                // Low HRV and High EDA -> Stressed (high value)
                // High HRV and Low EDA -> Calm (low value)
                const hrv = biometricState['Heart Rate Variability (HRV)'];
                const eda = biometricState['Electrodermal Activity (EDA)'];
                emotionalState['Calm vs. Stressed'] = (1 - hrv) * 0.5 + eda * 0.5;

                // Rule for 'Focused vs. Distracted'
                // High Alpha/Beta Ratio -> Focused (high value)
                emotionalState['Focused vs. Distracted'] = biometricState['Brainwave Ratio (Alpha/Beta)'];
            }


            // --- UI & RENDERING ---
            const cognitiveContainer = document.getElementById('cognitive-profile');
            const biometricContainer = document.getElementById('biometric-inputs');
            const emotionalContainer = document.getElementById('emotional-profile');
            const catalogContainer = document.getElementById('product-catalog');
            const recommendationsContainer = document.getElementById('recommendations');

            function createSliders(container, definitions, stateObj, isInteractive = true) {
                container.innerHTML = '';
                Object.keys(definitions).forEach(key => {
                    if (isInteractive) {
                        const value = stateObj[key];
                        const percentage = (value * 100).toFixed(0);
                        const sliderHTML = `
                            <div>
                                <label for="${key}" class="block text-sm font-medium text-slate-300">${key} <span class="text-xs text-slate-400">(0-1)</span></label>
                                <p class="text-xs text-slate-500 mb-2">${definitions[key]} <span class="text-sky-400">Current: ${percentage}</span></p>
                                <input type="range" id="${key}" name="${key}" min="0" max="1" step="0.1" value="${value}" class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer">
                            </div>
                        `;
                        container.insertAdjacentHTML('beforeend', sliderHTML);
                    } else {
                        const value = stateObj[key];
                        const percentage = (value * 100).toFixed(0);
                        const barHTML = `
                            <div>
                                <label class="block text-sm font-medium text-slate-300">${key}</label>
                                <p class="text-xs text-slate-500 mb-2">${definitions[key]}</p>
                                <div class="w-full derived-bar-bg rounded-full h-4">
                                    <div class="derived-bar-fill h-4 rounded-full text-right pr-2 text-xs text-black font-bold flex items-center justify-end" style="width: ${percentage}%">
                                        ${percentage}%
                                    </div>
                                </div>
                            </div>
                        `;
                         container.insertAdjacentHTML('beforeend', barHTML);
                    }
                });
            }
            
            function renderProfile() {
                createSliders(cognitiveContainer, COGNITIVE_TRAITS, cognitiveState, true);
                // Add a clarifying note for cognitive sliders
                const note = document.createElement('div');
                note.className = 'text-xs text-slate-400 mt-2';
                note.innerHTML = 'Move the sliders to simulate different customer cognitive traits. 0 = lowest, 1 = highest.';
                cognitiveContainer.appendChild(note);
                createSliders(biometricContainer, BIOMETRIC_INPUTS, biometricState, true);
                createSliders(emotionalContainer, EMOTIONAL_STATES, emotionalState, false); // Not interactive
                addProfileListeners();
            }

            function renderCatalog() {
                catalogContainer.innerHTML = '';
                PRODUCTS.forEach(product => {
                    const isSelected = product.id === selectedProductId;
                    const cardHTML = `
                        <div class="product-card card p-4 rounded-lg text-center ${isSelected ? 'selected' : ''}" data-id="${product.id}">
                            <div class="text-5xl">${product.emoji}</div>
                            <p class="mt-2 font-semibold text-sm text-white">${product.name}</p>
                        </div>
                    `;
                    catalogContainer.insertAdjacentHTML('beforeend', cardHTML);
                });
                addProductListeners();
            }

            function updateRecommendations() {
                let currentCognitiveVec = getVector(cognitiveState, Object.keys(COGNITIVE_TRAITS));
                let currentEmotionalVec = getVector(emotionalState, Object.keys(EMOTIONAL_STATES));

                if (selectedProductId) {
                    const product = PRODUCTS.find(p => p.id === selectedProductId);
                    currentCognitiveVec = projectState(currentCognitiveVec, getProductVector(product.traits, Object.keys(COGNITIVE_TRAITS)), 0.4);
                    currentEmotionalVec = projectState(currentEmotionalVec, getProductVector(product.emotion, Object.keys(EMOTIONAL_STATES)), 0.4);
                }

                const scoredProducts = PRODUCTS.map(product => {
                    const cogScore = dotProduct(currentCognitiveVec, getProductVector(product.traits, Object.keys(COGNITIVE_TRAITS)));
                    const emoScore = dotProduct(currentEmotionalVec, getProductVector(product.emotion, Object.keys(EMOTIONAL_STATES)));
                    const finalScore = (cogScore * COGNITIVE_WEIGHT) + (emoScore * EMOTIONAL_WEIGHT);
                    return { ...product, finalScore };
                }).sort((a, b) => b.finalScore - a.finalScore);

                recommendationsContainer.innerHTML = '';
                scoredProducts.forEach((product, index) => {
                    const scorePercentage = (product.finalScore * 100).toFixed(1);
                    const itemHTML = `
                        <div class="recommendation-item card flex items-center p-3 rounded-lg" style="order: ${index}">
                            <div class="text-3xl mr-4">${product.emoji}</div>
                            <div class="flex-grow">
                                <p class="font-semibold text-white">${product.name}</p>
                                <p class="text-sm text-slate-400">Total Alignment: ${scorePercentage}%</p>
                            </div>
                            <div class="w-24 h-4 bg-slate-700 rounded-full overflow-hidden">
                                <div class="bg-sky-500 h-full rounded-full" style="width: ${scorePercentage}%;"></div>
                            </div>
                        </div>
                    `;
                    recommendationsContainer.insertAdjacentHTML('beforeend', itemHTML);
                });
            }

            // --- EVENT LISTENERS ---
            function addProfileListeners() {
                const cognitiveKeys = Object.keys(COGNITIVE_TRAITS);
                const biometricKeys = Object.keys(BIOMETRIC_INPUTS);

                cognitiveKeys.forEach(key => {
                    document.getElementById(key).addEventListener('input', (e) => {
                        cognitiveState[key] = parseFloat(e.target.value);
                        updateAll();
                    });
                });

                biometricKeys.forEach(key => {
                     document.getElementById(key).addEventListener('input', (e) => {
                        biometricState[key] = parseFloat(e.target.value);
                        updateAll();
                    });
                });
            }

            function addProductListeners() {
                document.querySelectorAll('.product-card').forEach(card => {
                    card.addEventListener('click', (e) => {
                        const newId = parseInt(e.currentTarget.dataset.id);
                        selectedProductId = (selectedProductId === newId) ? null : newId;
                        renderCatalog();
                        updateRecommendations();
                    });
                });
            }

            function updateAll() {
                selectedProductId = null; // Reset context on profile change
                deriveEmotionalState();
                createSliders(emotionalContainer, EMOTIONAL_STATES, emotionalState, false); // Re-render derived state
                renderCatalog();
                updateRecommendations();
            }

            // --- INITIALIZATION ---
            function init() {
                Object.keys(COGNITIVE_TRAITS).forEach(key => cognitiveState[key] = 0.5);
                Object.keys(BIOMETRIC_INPUTS).forEach(key => biometricState[key] = 0.5);
                deriveEmotionalState();
                
                renderProfile();
                renderCatalog();
                updateRecommendations();
            }

            init();
        });
    </script>
</body>
</html>
'''

@app.route('/derive_emotion', methods=['POST'])
def derive_emotion_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    emotion = derive_emotion(data)
    return jsonify({'emotional_state': emotion})

@app.route('/recommend', methods=['POST'])
def recommend_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    strategy, scores = recommend_strategy(data)
    return jsonify({'strategy': strategy, 'scores': scores})

if __name__ == '__main__':
    app.run(debug=True)
