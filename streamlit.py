import streamlit as st
from streamlit.components.v1 import html

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Born - Sélecteur Stratégique</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --red-primary: #DC2626;
            --red-dark: #991B1B;
            --red-light: #EF4444;
            --black: #0A0A0A;
            --gray-dark: #1F2937;
            --gray-medium: #4B5563;
            --gray-light: #9CA3AF;
            --gray-lighter: #E5E7EB;
            --white: #FFFFFF;
            --blue-primary: #2563EB;
            --blue-dark: #1E40AF;
            --blue-light: #3B82F6;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--black);
            min-height: 100vh;
            color: var(--white);
            position: relative;
            overflow-x: hidden;
        }

        /* Background Animation */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(220, 38, 38, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 80% 50%, rgba(220, 38, 38, 0.1) 0%, transparent 50%),
                var(--black);
            z-index: -1;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Header avec Logo */
        .header {
            background: linear-gradient(135deg, var(--black) 0%, var(--gray-dark) 100%);
            border: 1px solid rgba(220, 38, 38, 0.3);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 60px rgba(220, 38, 38, 0.1);
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(220, 38, 38, 0.3), transparent);
            animation: headerShine 3s infinite;
        }

        @keyframes headerShine {
            100% { left: 100%; }
        }

        .logo-container {
            display: inline-flex;
            align-items: center;
            margin-bottom: 20px;
            position: relative;
        }

        .logo {
            width: 80px;
            height: 80px;
            position: relative;
            margin-right: 20px;
        }

        .logo-circle {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 4px solid var(--gray-medium);
            border-radius: 50%;
            animation: rotateCircle 20s linear infinite;
        }

        @keyframes rotateCircle {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .logo-text {
            font-size: 2.5em;
            font-weight: 300;
        }

        .logo-text .born {
            color: var(--red-primary);
            font-weight: 700;
        }

        .logo-text .global {
            color: var(--gray-light);
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(135deg, var(--white) 0%, var(--gray-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            color: var(--gray-light);
            font-size: 1.1em;
        }

        /* Main Category Buttons */
        .category-selector {
            display: flex;
            gap: 20px;
            margin-top: 30px;
            justify-content: center;
        }

        .category-btn {
            flex: 1;
            max-width: 300px;
            padding: 25px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid transparent;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
        }

        .category-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .category-btn.active {
            border-color: var(--red-primary);
            background: rgba(220, 38, 38, 0.1);
            box-shadow: 0 10px 30px rgba(220, 38, 38, 0.3);
        }

        .category-btn.enterprises.active {
            border-color: var(--blue-primary);
            background: rgba(37, 99, 235, 0.1);
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.3);
        }

        .category-icon {
            font-size: 3em;
            margin-bottom: 10px;
        }

        .category-title {
            font-size: 1.3em;
            font-weight: 600;
            color: var(--white);
            margin-bottom: 5px;
        }

        .category-desc {
            font-size: 0.9em;
            color: var(--gray-light);
        }

        .total-counter {
            background: rgba(220, 38, 38, 0.1);
            border: 1px solid rgba(220, 38, 38, 0.3);
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            display: inline-block;
            backdrop-filter: blur(10px);
            transition: all 0.3s;
        }

        .total-counter.enterprises {
            background: rgba(37, 99, 235, 0.1);
            border-color: rgba(37, 99, 235, 0.3);
        }

        .total-counter .number {
            font-size: 3em;
            font-weight: 700;
            color: var(--red-primary);
            text-shadow: 0 0 20px rgba(220, 38, 38, 0.5);
        }

        .total-counter.enterprises .number {
            color: var(--blue-primary);
            text-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
        }

        .total-counter .label {
            color: var(--gray-light);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.9em;
        }

        /* Content */
        .content {
            margin-top: 30px;
        }

        .category-content {
            display: none;
        }

        .category-content.active {
            display: block;
            animation: fadeIn 0.5s;
        }

        /* Tabs */
        .tabs {
            display: flex;
            background: var(--gray-dark);
            border-radius: 15px;
            padding: 5px;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }

        .tab {
            flex: 1;
            padding: 18px 25px;
            text-align: center;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 600;
            color: var(--gray-light);
            position: relative;
            overflow: hidden;
        }

        .tab::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--red-primary);
            transform: translateY(100%);
            transition: transform 0.3s;
            z-index: -1;
        }

        .enterprises .tab::before {
            background: var(--blue-primary);
        }

        .tab:hover::before {
            transform: translateY(0);
        }

        .tab:hover {
            color: var(--white);
            transform: translateY(-2px);
        }

        .tab.active {
            background: var(--red-primary);
            color: var(--white);
            box-shadow: 0 4px 20px rgba(220, 38, 38, 0.4);
        }

        .enterprises .tab.active {
            background: var(--blue-primary);
            box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.5s;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Region Cards */
        .region-card {
            background: var(--gray-dark);
            border: 1px solid rgba(220, 38, 38, 0.2);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .enterprises .region-card {
            border-color: rgba(37, 99, 235, 0.2);
        }

        .region-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--red-primary);
            transition: width 0.3s;
        }

        .enterprises .region-card::before {
            background: var(--blue-primary);
        }

        .region-card:hover {
            transform: translateX(5px);
            box-shadow: 0 10px 30px rgba(220, 38, 38, 0.2);
            border-color: rgba(220, 38, 38, 0.4);
        }

        .enterprises .region-card:hover {
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.2);
            border-color: rgba(37, 99, 235, 0.4);
        }

        .region-card:hover::before {
            width: 8px;
        }

        .region-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .region-name {
            font-size: 1.3em;
            font-weight: 600;
            color: var(--white);
        }

        .priority-badge {
            background: var(--red-primary);
            color: var(--white);
            padding: 6px 15px;
            border-radius: 25px;
            font-size: 0.9em;
            font-weight: 600;
            box-shadow: 0 2px 10px rgba(220, 38, 38, 0.3);
        }

        .enterprises .priority-badge {
            background: var(--blue-primary);
            box-shadow: 0 2px 10px rgba(37, 99, 235, 0.3);
        }

        /* Sliders */
        .slider-container {
            margin: 20px 0;
        }

        .slider-label {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            color: var(--gray-light);
        }

        .slider-label span:last-child {
            color: var(--red-primary);
            font-weight: 700;
            font-size: 1.2em;
        }

        .enterprises .slider-label span:last-child {
            color: var(--blue-primary);
        }

        .slider {
            width: 100%;
            height: 8px;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.1);
            outline: none;
            -webkit-appearance: none;
            cursor: pointer;
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--red-primary);
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(220, 38, 38, 0.4);
            transition: all 0.3s;
        }

        .enterprises .slider::-webkit-slider-thumb {
            background: var(--blue-primary);
            box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
        }

        .slider::-webkit-slider-thumb:hover {
            transform: scale(1.2);
            box-shadow: 0 2px 20px rgba(220, 38, 38, 0.6);
        }

        .enterprises .slider::-webkit-slider-thumb:hover {
            box-shadow: 0 2px 20px rgba(37, 99, 235, 0.6);
        }

        .slider::-moz-range-thumb {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--red-primary);
            cursor: pointer;
            border: none;
            box-shadow: 0 2px 10px rgba(220, 38, 38, 0.4);
            transition: all 0.3s;
        }

        .enterprises .slider::-moz-range-thumb {
            background: var(--blue-primary);
            box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--red-primary), var(--red-light));
            transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .enterprises .progress-fill {
            background: linear-gradient(90deg, var(--blue-primary), var(--blue-light));
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            animation: progressShine 2s infinite;
        }

        @keyframes progressShine {
            from { transform: translateX(-100%); }
            to { transform: translateX(100%); }
        }

        .countries-list {
            font-size: 0.9em;
            color: var(--gray-light);
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Action Buttons */
        .action-buttons {
            display: flex;
            gap: 20px;
            margin-top: 40px;
        }

        .btn {
            flex: 1;
            padding: 18px 30px;
            border: none;
            border-radius: 12px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .btn:hover::before {
            width: 300px;
            height: 300px;
        }

        .btn-primary {
            background: var(--red-primary);
            color: var(--white);
            box-shadow: 0 4px 20px rgba(220, 38, 38, 0.3);
        }

        .enterprises .btn-primary {
            background: var(--blue-primary);
            box-shadow: 0 4px 20px rgba(37, 99, 235, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(220, 38, 38, 0.5);
        }

        .enterprises .btn-primary:hover {
            box-shadow: 0 8px 30px rgba(37, 99, 235, 0.5);
        }

        .btn-success {
            background: var(--gray-dark);
            color: var(--white);
            border: 2px solid var(--red-primary);
        }

        .enterprises .btn-success {
            border-color: var(--blue-primary);
        }

        .btn-success:hover {
            background: var(--red-primary);
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(220, 38, 38, 0.5);
        }

        .enterprises .btn-success:hover {
            background: var(--blue-primary);
            box-shadow: 0 8px 30px rgba(37, 99, 235, 0.5);
        }

        /* Preview Section */
        .preview-section {
            background: var(--gray-dark);
            border: 1px solid rgba(220, 38, 38, 0.2);
            border-radius: 20px;
            padding: 30px;
            margin-top: 30px;
            animation: slideUp 0.5s;
        }

        .enterprises .preview-section {
            border-color: rgba(37, 99, 235, 0.2);
        }

        @keyframes slideUp {
            from { 
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .preview-section h3 {
            color: var(--white);
            margin-bottom: 25px;
            font-size: 1.5em;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .stat-card {
            background: rgba(220, 38, 38, 0.1);
            border: 1px solid rgba(220, 38, 38, 0.3);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            transition: all 0.3s;
        }

        .enterprises .stat-card {
            background: rgba(37, 99, 235, 0.1);
            border-color: rgba(37, 99, 235, 0.3);
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(220, 38, 38, 0.3);
            border-color: var(--red-primary);
        }

        .enterprises .stat-card:hover {
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.3);
            border-color: var(--blue-primary);
        }

        .stat-number {
            font-size: 2.5em;
            font-weight: 700;
            color: var(--red-primary);
            display: block;
            text-shadow: 0 0 20px rgba(220, 38, 38, 0.5);
        }

        .enterprises .stat-number {
            color: var(--blue-primary);
            text-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
        }

        .stat-label {
            color: var(--gray-light);
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.9em;
        }

        .preview-item {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid var(--red-primary);
            transition: all 0.3s;
        }

        .enterprises .preview-item {
            border-left-color: var(--blue-primary);
        }

        .preview-item:hover {
            transform: translateX(10px);
            background: rgba(220, 38, 38, 0.1);
            box-shadow: 0 5px 20px rgba(220, 38, 38, 0.2);
        }

        .enterprises .preview-item:hover {
            background: rgba(37, 99, 235, 0.1);
            box-shadow: 0 5px 20px rgba(37, 99, 235, 0.2);
        }

        .preview-name {
            font-weight: 600;
            color: var(--white);
            margin-bottom: 8px;
            font-size: 1.1em;
        }

        .preview-details {
            font-size: 0.9em;
            color: var(--gray-light);
        }

        /* Mobile Responsive */
        @media (max-width: 768px) {
            .header {
                padding: 30px 20px;
            }
            
            .logo-container {
                flex-direction: column;
                text-align: center;
            }
            
            .logo {
                margin-right: 0;
                margin-bottom: 20px;
            }
            
            .category-selector {
                flex-direction: column;
            }
            
            .tabs {
                flex-direction: column;
                gap: 10px;
            }
            
            .action-buttons {
                flex-direction: column;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Loading Animation */
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: var(--red-primary);
            animation: spin 1s ease-in-out infinite;
        }

        .enterprises .loading {
            border-top-color: var(--blue-primary);
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo-container">
                <div class="logo">
                    <div class="logo-circle"></div>
                </div>
                <div class="logo-text">
                    <span class="born">born</span><span class="global">global</span>
                </div>
            </div>
            <h1>Sélecteur Stratégique</h1>
            <p>Configurez votre sélection d'universités et d'entreprises selon vos critères stratégiques</p>
            
            <div class="category-selector">
                <div class="category-btn active" onclick="switchCategory('universities')">
                    <div class="category-icon">🎓</div>
                    <div class="category-title">Universités</div>
                    <div class="category-desc">Sélection des top 1000</div>
                </div>
                <div class="category-btn enterprises" onclick="switchCategory('enterprises')">
                    <div class="category-icon">🏢</div>
                    <div class="category-title">Entreprises</div>
                    <div class="category-desc">Sélection des top 1000</div>
                </div>
            </div>
            
            <div class="total-counter" id="universities-counter">
                <div class="number" id="totalUniversities">1000</div>
                <div class="label">Universités Total</div>
            </div>
            <div class="total-counter enterprises" id="enterprises-counter" style="display: none;">
                <div class="number" id="totalEnterprises">1000</div>
                <div class="label">Entreprises Total</div>
            </div>
        </div>

        <!-- Universities Content -->
        <div class="content category-content active" id="universities-content">
            <!-- Tabs -->
            <div class="tabs">
                <div class="tab active" onclick="switchTab('uni-regions', event)">🌍 Régions</div>
                <div class="tab" onclick="switchTab('uni-types', event)">🏛️ Types</div>
                <div class="tab" onclick="switchTab('uni-criteria', event)">📊 Critères</div>
            </div>

            <!-- Regions Tab -->
            <div id="uni-regions" class="tab-content active">
                <h2 style="color: var(--white); margin-bottom: 30px;">Répartition Géographique</h2>
                
                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇨🇳 Asie Prioritaire</span>
                        <span class="priority-badge">Priorité 10</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="asie-value">250</span>
                        </div>
                        <input type="range" class="slider" id="asie-slider" min="0" max="400" value="250" oninput="updateQuota('asie', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="asie-progress" style="width: 62.5%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Chine, Japon, Corée du Sud, Inde, Taiwan, Hong Kong</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇺🇸 Amérique du Nord</span>
                        <span class="priority-badge">Priorité 10</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="amerique-value">200</span>
                        </div>
                        <input type="range" class="slider" id="amerique-slider" min="0" max="400" value="200" oninput="updateQuota('amerique', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="amerique-progress" style="width: 50%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: États-Unis, Canada</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇸🇬 Asie Sud-Est</span>
                        <span class="priority-badge">Priorité 9</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="sudest-value">180</span>
                        </div>
                        <input type="range" class="slider" id="sudest-slider" min="0" max="400" value="180" oninput="updateQuota('sudest', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="sudest-progress" style="width: 45%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Singapour, Malaisie, Thaïlande, Vietnam, Indonésie, Philippines</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇦🇪 Péninsule Arabique</span>
                        <span class="priority-badge">Priorité 9</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="arabique-value">120</span>
                        </div>
                        <input type="range" class="slider" id="arabique-slider" min="0" max="400" value="120" oninput="updateQuota('arabique', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="arabique-progress" style="width: 30%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: EAU, Arabie Saoudite, Qatar, Koweït, Bahreïn, Oman</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇿🇦 Afrique Subsaharienne</span>
                        <span class="priority-badge">Priorité 8</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="afrique-value">150</span>
                        </div>
                        <input type="range" class="slider" id="afrique-slider" min="0" max="400" value="150" oninput="updateQuota('afrique', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="afrique-progress" style="width: 37.5%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Afrique du Sud, Nigeria, Kenya, Ghana, Éthiopie, Uganda</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇩🇪 Europe Sélective</span>
                        <span class="priority-badge">Priorité 7</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="europe-value">100</span>
                        </div>
                        <input type="range" class="slider" id="europe-slider" min="0" max="400" value="100" oninput="updateQuota('europe', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="europe-progress" style="width: 25%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Allemagne, Royaume-Uni, Pays-Bas, Suède, Suisse, Norvège</div>
                </div>
            </div>

            <!-- Types Tab -->
            <div id="uni-types" class="tab-content">
                <h2 style="color: var(--white); margin-bottom: 30px;">Types d'Universités (% de la sélection)</h2>
                
                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🔬 Research Intensive</span>
                        <span class="priority-badge" id="research-percent">40%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="research-slider" min="0" max="60" value="40" oninput="updateType('research', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="research-progress" style="width: 66.7%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💻 Technology Focused</span>
                        <span class="priority-badge" id="tech-percent">25%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="tech-slider" min="0" max="60" value="25" oninput="updateType('tech', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="tech-progress" style="width: 41.7%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💼 Business Oriented</span>
                        <span class="priority-badge" id="business-percent">20%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="business-slider" min="0" max="60" value="20" oninput="updateType('business', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="business-progress" style="width: 33.3%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🌍 International Programs</span>
                        <span class="priority-badge" id="international-percent">10%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="international-slider" min="0" max="60" value="10" oninput="updateType('international', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="international-progress" style="width: 16.7%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">⭐ Specialized</span>
                        <span class="priority-badge" id="specialized-percent">5%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="specialized-slider" min="0" max="60" value="5" oninput="updateType('specialized', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="specialized-progress" style="width: 8.3%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Criteria Tab -->
            <div id="uni-criteria" class="tab-content">
                <h2 style="color: var(--white); margin-bottom: 30px;">Critères de Sélection (Pondération 1-10)</h2>
                
                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🏆 International Ranking</span>
                        <span class="priority-badge" id="ranking-score">8/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ranking-slider" min="1" max="10" value="8" oninput="updateCriteria('ranking', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ranking-progress" style="width: 80%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🔬 Research Output</span>
                        <span class="priority-badge" id="research-score">7/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="research-criteria-slider" min="1" max="10" value="7" oninput="updateCriteria('research-criteria', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="research-criteria-progress" style="width: 70%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🤝 Industry Partnerships</span>
                        <span class="priority-badge" id="industry-score">9/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="industry-slider" min="1" max="10" value="9" oninput="updateCriteria('industry', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="industry-progress" style="width: 90%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💻 Digitalization</span>
                        <span class="priority-badge" id="digital-score">8/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="digital-slider" min="1" max="10" value="8" oninput="updateCriteria('digital', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="digital-progress" style="width: 80%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🚀 Entrepreneurship</span>
                        <span class="priority-badge" id="entrepreneur-score">7/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="entrepreneur-slider" min="1" max="10" value="7" oninput="updateCriteria('entrepreneur', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="entrepreneur-progress" style="width: 70%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="action-buttons">
                <button class="btn btn-primary" onclick="generatePreview('universities')">
                    📊 Générer Aperçu
                </button>
                <button class="btn btn-success" onclick="exportConfiguration('universities')">
                    💾 Exporter Configuration
                </button>
            </div>

            <!-- Preview Section -->
            <div class="preview-section" id="universities-preview" style="display: none;">
                <h3>📋 Aperçu de la Sélection</h3>
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="stat-number" id="uni-previewTotal">1000</span>
                        <div class="stat-label">Total Universités</div>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number" id="uni-previewCountries">25</span>
                        <div class="stat-label">Pays Couverts</div>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number" id="uni-previewScore">8.2</span>
                        <div class="stat-label">Score Moyen</div>
                    </div>
                </div>
                
                <div id="uni-previewResults"></div>
            </div>
        </div>

        <!-- Enterprises Content -->
        <div class="content category-content enterprises" id="enterprises-content">
            <!-- Tabs -->
            <div class="tabs">
                <div class="tab active" onclick="switchTab('ent-regions', event)">🌍 Régions</div>
                <div class="tab" onclick="switchTab('ent-sectors', event)">🏭 Secteurs</div>
                <div class="tab" onclick="switchTab('ent-criteria', event)">📊 Critères</div>
            </div>

            <!-- Regions Tab -->
            <div id="ent-regions" class="tab-content active">
                <h2 style="color: var(--white); margin-bottom: 30px;">Répartition Géographique</h2>
                
                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇺🇸 Amérique du Nord</span>
                        <span class="priority-badge">Priorité 10</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="ent-amerique-value">300</span>
                        </div>
                        <input type="range" class="slider" id="ent-amerique-slider" min="0" max="400" value="300" oninput="updateEntQuota('amerique', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-amerique-progress" style="width: 75%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: États-Unis, Canada</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇨🇳 Asie-Pacifique</span>
                        <span class="priority-badge">Priorité 10</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="ent-asie-value">250</span>
                        </div>
                        <input type="range" class="slider" id="ent-asie-slider" min="0" max="400" value="250" oninput="updateEntQuota('asie', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-asie-progress" style="width: 62.5%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Chine, Japon, Corée du Sud, Inde, Taiwan, Australie</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇪🇺 Europe</span>
                        <span class="priority-badge">Priorité 9</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="ent-europe-value">200</span>
                        </div>
                        <input type="range" class="slider" id="ent-europe-slider" min="0" max="400" value="200" oninput="updateEntQuota('europe', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-europe-progress" style="width: 50%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Allemagne, France, Royaume-Uni, Suisse, Pays-Bas, Suède</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🇦🇪 Moyen-Orient</span>
                        <span class="priority-badge">Priorité 8</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="ent-moyenorient-value">100</span>
                        </div>
                        <input type="range" class="slider" id="ent-moyenorient-slider" min="0" max="400" value="100" oninput="updateEntQuota('moyenorient', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-moyenorient-progress" style="width: 25%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: EAU, Arabie Saoudite, Qatar, Israël, Turquie</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🌎 Amérique Latine</span>
                        <span class="priority-badge">Priorité 7</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="ent-latam-value">80</span>
                        </div>
                        <input type="range" class="slider" id="ent-latam-slider" min="0" max="400" value="80" oninput="updateEntQuota('latam', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-latam-progress" style="width: 20%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Brésil, Mexique, Argentine, Chili, Colombie</div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🌍 Afrique</span>
                        <span class="priority-badge">Priorité 7</span>
                    </div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Quota:</span>
                            <span id="ent-afrique-value">70</span>
                        </div>
                        <input type="range" class="slider" id="ent-afrique-slider" min="0" max="400" value="70" oninput="updateEntQuota('afrique', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-afrique-progress" style="width: 17.5%"></div>
                        </div>
                    </div>
                    <div class="countries-list">Pays: Afrique du Sud, Nigeria, Kenya, Égypte, Maroc</div>
                </div>
            </div>

            <!-- Sectors Tab -->
            <div id="ent-sectors" class="tab-content">
                <h2 style="color: var(--white); margin-bottom: 30px;">Secteurs d'Activité (% de la sélection)</h2>
                
                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💻 Technologie</span>
                        <span class="priority-badge" id="ent-tech-percent">30%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-tech-slider" min="0" max="50" value="30" oninput="updateEntSector('tech', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-tech-progress" style="width: 60%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💊 Pharmaceutique/Santé</span>
                        <span class="priority-badge" id="ent-pharma-percent">20%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-pharma-slider" min="0" max="50" value="20" oninput="updateEntSector('pharma', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-pharma-progress" style="width: 40%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🏦 Services Financiers</span>
                        <span class="priority-badge" id="ent-finance-percent">15%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-finance-slider" min="0" max="50" value="15" oninput="updateEntSector('finance', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-finance-progress" style="width: 30%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">⚡ Énergie/Environnement</span>
                        <span class="priority-badge" id="ent-energy-percent">15%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-energy-slider" min="0" max="50" value="15" oninput="updateEntSector('energy', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-energy-progress" style="width: 30%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🚗 Industrie/Automobile</span>
                        <span class="priority-badge" id="ent-industry-percent">10%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-industry-slider" min="0" max="50" value="10" oninput="updateEntSector('industry', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-industry-progress" style="width: 20%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🛍️ Commerce/Luxe</span>
                        <span class="priority-badge" id="ent-retail-percent">10%</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-retail-slider" min="0" max="50" value="10" oninput="updateEntSector('retail', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-retail-progress" style="width: 20%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Criteria Tab -->
            <div id="ent-criteria" class="tab-content">
                <h2 style="color: var(--white); margin-bottom: 30px;">Critères de Sélection (Pondération 1-10)</h2>
                
                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💰 Chiffre d'Affaires</span>
                        <span class="priority-badge" id="ent-revenue-score">9/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-revenue-slider" min="1" max="10" value="9" oninput="updateEntCriteria('revenue', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-revenue-progress" style="width: 90%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">📈 Croissance</span>
                        <span class="priority-badge" id="ent-growth-score">8/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-growth-slider" min="1" max="10" value="8" oninput="updateEntCriteria('growth', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-growth-progress" style="width: 80%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">💡 Innovation</span>
                        <span class="priority-badge" id="ent-innovation-score">9/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-innovation-slider" min="1" max="10" value="9" oninput="updateEntCriteria('innovation', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-innovation-progress" style="width: 90%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🌱 RSE/Durabilité</span>
                        <span class="priority-badge" id="ent-sustainability-score">7/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-sustainability-slider" min="1" max="10" value="7" oninput="updateEntCriteria('sustainability', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-sustainability-progress" style="width: 70%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">🌐 Présence Internationale</span>
                        <span class="priority-badge" id="ent-international-score">8/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-international-slider" min="1" max="10" value="8" oninput="updateEntCriteria('international', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-international-progress" style="width: 80%"></div>
                        </div>
                    </div>
                </div>

                <div class="region-card">
                    <div class="region-header">
                        <span class="region-name">👥 Capital Humain</span>
                        <span class="priority-badge" id="ent-human-score">6/10</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" class="slider" id="ent-human-slider" min="1" max="10" value="6" oninput="updateEntCriteria('human', this.value)">
                        <div class="progress-bar">
                            <div class="progress-fill" id="ent-human-progress" style="width: 60%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="action-buttons">
                <button class="btn btn-primary" onclick="generatePreview('enterprises')">
                    📊 Générer Aperçu
                </button>
                <button class="btn btn-success" onclick="exportConfiguration('enterprises')">
                    💾 Exporter Configuration
                </button>
            </div>

            <!-- Preview Section -->
            <div class="preview-section" id="enterprises-preview" style="display: none;">
                <h3>📋 Aperçu de la Sélection</h3>
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="stat-number" id="ent-previewTotal">1000</span>
                        <div class="stat-label">Total Entreprises</div>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number" id="ent-previewCountries">30</span>
                        <div class="stat-label">Pays Couverts</div>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number" id="ent-previewScore">7.8</span>
                        <div class="stat-label">Score Moyen</div>
                    </div>
                </div>
                
                <div id="ent-previewResults"></div>
            </div>
        </div>
    </div>

    <script>
        // Configuration globale
        let config = {
            universities: {
                regions: {
                    asie: 250,
                    amerique: 200,
                    sudest: 180,
                    arabique: 120,
                    afrique: 150,
                    europe: 100
                },
                types: {
                    research: 40,
                    tech: 25,
                    business: 20,
                    international: 10,
                    specialized: 5
                },
                criteria: {
                    ranking: 8,
                    'research-criteria': 7,
                    industry: 9,
                    digital: 8,
                    entrepreneur: 7
                }
            },
            enterprises: {
                regions: {
                    amerique: 300,
                    asie: 250,
                    europe: 200,
                    moyenorient: 100,
                    latam: 80,
                    afrique: 70
                },
                sectors: {
                    tech: 30,
                    pharma: 20,
                    finance: 15,
                    energy: 15,
                    industry: 10,
                    retail: 10
                },
                criteria: {
                    revenue: 9,
                    growth: 8,
                    innovation: 9,
                    sustainability: 7,
                    international: 8,
                    human: 6
                }
            }
        };

        let currentCategory = 'universities';

        function switchCategory(category) {
            currentCategory = category;
            
            // Update buttons
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.closest('.category-btn').classList.add('active');
            
            // Update counters
            if (category === 'universities') {
                document.getElementById('universities-counter').style.display = 'inline-block';
                document.getElementById('enterprises-counter').style.display = 'none';
                document.getElementById('universities-content').classList.add('active');
                document.getElementById('enterprises-content').classList.remove('active');
            } else {
                document.getElementById('universities-counter').style.display = 'none';
                document.getElementById('enterprises-counter').style.display = 'inline-block';
                document.getElementById('universities-content').classList.remove('active');
                document.getElementById('enterprises-content').classList.add('active');
            }
        }

        function switchTab(tabName, event) {
            const parentContent = event.target.closest('.category-content');
            
            // Cacher tous les contenus dans cette catégorie
            parentContent.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Désactiver tous les onglets dans cette catégorie
            parentContent.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Activer l'onglet et contenu sélectionné
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }

        // Universities functions
        function updateQuota(region, value) {
            config.universities.regions[region] = parseInt(value);
            
            const valueElement = document.getElementById(region + '-value');
            valueElement.textContent = value;
            valueElement.style.animation = 'pulse 0.3s';
            
            const progress = document.getElementById(region + '-progress');
            progress.style.width = (value / 400 * 100) + '%';
            
            setTimeout(() => {
                valueElement.style.animation = '';
            }, 300);
            
            updateTotal('universities');
        }

        function updateType(type, value) {
            config.universities.types[type] = parseInt(value);
            
            const percentElement = document.getElementById(type + '-percent');
            percentElement.textContent = value + '%';
            percentElement.style.animation = 'pulse 0.3s';
            
            document.getElementById(type + '-progress').style.width = (value / 60 * 100) + '%';
            
            setTimeout(() => {
                percentElement.style.animation = '';
            }, 300);
        }

        function updateCriteria(criterion, value) {
            config.universities.criteria[criterion] = parseInt(value);
            
            const scoreElement = document.getElementById(criterion + '-score');
            scoreElement.textContent = value + '/10';
            scoreElement.style.animation = 'pulse 0.3s';
            
            document.getElementById(criterion + '-progress').style.width = (value / 10 * 100) + '%';
            
            setTimeout(() => {
                scoreElement.style.animation = '';
            }, 300);
        }

        // Enterprises functions
        function updateEntQuota(region, value) {
            config.enterprises.regions[region] = parseInt(value);
            
            const valueElement = document.getElementById('ent-' + region + '-value');
            valueElement.textContent = value;
            valueElement.style.animation = 'pulse 0.3s';
            
            const progress = document.getElementById('ent-' + region + '-progress');
            progress.style.width = (value / 400 * 100) + '%';
            
            setTimeout(() => {
                valueElement.style.animation = '';
            }, 300);
            
            updateTotal('enterprises');
        }

        function updateEntSector(sector, value) {
            config.enterprises.sectors[sector] = parseInt(value);
            
            const percentElement = document.getElementById('ent-' + sector + '-percent');
            percentElement.textContent = value + '%';
            percentElement.style.animation = 'pulse 0.3s';
            
            document.getElementById('ent-' + sector + '-progress').style.width = (value / 50 * 100) + '%';
            
            setTimeout(() => {
                percentElement.style.animation = '';
            }, 300);
        }

        function updateEntCriteria(criterion, value) {
            config.enterprises.criteria[criterion] = parseInt(value);
            
            const scoreElement = document.getElementById('ent-' + criterion + '-score');
            scoreElement.textContent = value + '/10';
            scoreElement.style.animation = 'pulse 0.3s';
            
            document.getElementById('ent-' + criterion + '-progress').style.width = (value / 10 * 100) + '%';
            
            setTimeout(() => {
                scoreElement.style.animation = '';
            }, 300);
        }

        function updateTotal(category) {
            const total = Object.values(config[category].regions).reduce((sum, value) => sum + value, 0);
            const totalElement = document.getElementById(category === 'universities' ? 'totalUniversities' : 'totalEnterprises');
            totalElement.textContent = total;
            totalElement.style.animation = 'pulse 0.5s';
            
            setTimeout(() => {
                totalElement.style.animation = '';
            }, 500);
        }

        function generatePreview(category) {
            const data = config[category];
            const total = Object.values(data.regions).reduce((sum, value) => sum + value, 0);
            
            let totalCountries, avgScore, samples;
            
            if (category === 'universities') {
                const countries = {
                    asie: 6, amerique: 2, sudest: 6, arabique: 6, afrique: 6, europe: 6
                };
                totalCountries = Object.entries(data.regions)
                    .filter(([region, quota]) => quota > 0)
                    .reduce((sum, [region]) => sum + countries[region], 0);
                
                avgScore = Object.values(data.criteria).reduce((sum, value) => sum + value, 0) / Object.values(data.criteria).length;
                
                samples = [
                    { name: "Beijing International Business University", country: "🇨🇳 Chine", region: "Asie Prioritaire", score: 9.8 },
                    { name: "Stanford Technology Institute", country: "🇺🇸 États-Unis", region: "Amérique du Nord", score: 9.9 },
                    { name: "Singapore Digital Innovation University", country: "🇸🇬 Singapour", region: "Asie Sud-Est", score: 9.5 },
                    { name: "Dubai International University", country: "🇦🇪 EAU", region: "Péninsule Arabique", score: 9.2 },
                    { name: "Cape Town Research University", country: "🇿🇦 Afrique du Sud", region: "Afrique Subsaharienne", score: 8.8 },
                    { name: "Berlin Institute of Technology", country: "🇩🇪 Allemagne", region: "Europe Sélective", score: 9.0 }
                ];
                
                document.getElementById('uni-previewTotal').textContent = total;
                document.getElementById('uni-previewCountries').textContent = totalCountries;
                document.getElementById('uni-previewScore').textContent = avgScore.toFixed(1);
            } else {
                const countries = {
                    amerique: 2, asie: 6, europe: 6, moyenorient: 5, latam: 5, afrique: 5
                };
                totalCountries = Object.entries(data.regions)
                    .filter(([region, quota]) => quota > 0)
                    .reduce((sum, [region]) => sum + countries[region], 0);
                
                avgScore = Object.values(data.criteria).reduce((sum, value) => sum + value, 0) / Object.values(data.criteria).length;
                
                samples = [
                    { name: "Apple Inc.", country: "🇺🇸 États-Unis", sector: "Technologie", score: 9.9 },
                    { name: "Toyota Motor Corporation", country: "🇯🇵 Japon", sector: "Automobile", score: 9.2 },
                    { name: "Nestlé S.A.", country: "🇨🇭 Suisse", sector: "Alimentaire", score: 8.8 },
                    { name: "Saudi Aramco", country: "🇸🇦 Arabie Saoudite", sector: "Énergie", score: 9.5 },
                    { name: "Tencent Holdings", country: "🇨🇳 Chine", sector: "Technologie", score: 9.3 },
                    { name: "LVMH", country: "🇫🇷 France", sector: "Luxe", score: 9.0 }
                ];
                
                document.getElementById('ent-previewTotal').textContent = total;
                document.getElementById('ent-previewCountries').textContent = totalCountries;
                document.getElementById('ent-previewScore').textContent = avgScore.toFixed(1);
            }

            const previewHTML = samples.map(item => `
                <div class="preview-item">
                    <div class="preview-name">${item.name}</div>
                    <div class="preview-details">
                        ${item.country} • ${item.region || item.sector} • Score: ${item.score}/10
                    </div>
                </div>
            `).join('');

            const resultsId = category === 'universities' ? 'uni-previewResults' : 'ent-previewResults';
            const previewId = category === 'universities' ? 'universities-preview' : 'enterprises-preview';
            
            document.getElementById(resultsId).innerHTML = previewHTML;
            document.getElementById(previewId).style.display = 'block';
            
            // Scroll to preview
            document.getElementById(previewId).scrollIntoView({ behavior: 'smooth' });
        }

        function exportConfiguration(category) {
            const data = config[category];
            const exportData = {
                timestamp: new Date().toISOString(),
                category: category,
                configuration: {
                    totalItems: Object.values(data.regions).reduce((sum, value) => sum + value, 0),
                    regions: data.regions,
                    [category === 'universities' ? 'types' : 'sectors']: category === 'universities' ? data.types : data.sectors,
                    criteria: data.criteria
                },
                generatedBy: "Global Born Strategic Selector"
            };
            
            const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `global-born-${category}-config-${new Date().toISOString().split('T')[0]}.json`;
            a.click();
            URL.revokeObjectURL(url);
            
            // Animation de succès
            const btn = event.target;
            btn.innerHTML = '✅ Exporté!';
            btn.style.background = category === 'universities' ? 'var(--red-primary)' : 'var(--blue-primary)';
            
            setTimeout(() => {
                btn.innerHTML = '💾 Exporter Configuration';
                btn.style.background = '';
            }, 2000);
        }

        // Effet de pulsation pour les animations
        const style = document.createElement('style');
        style.textContent = `
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
        `;
        document.head.appendChild(style);

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {
            updateTotal('universities');
            updateTotal('enterprises');
        });
    </script>
</body>
</html>

st.components.v1.html(html_code, height=1000, scrolling=True)
