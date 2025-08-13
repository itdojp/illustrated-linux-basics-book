---
layout: chapter
title: "第4章：コンテナ入門"
chapter: 4
---
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第4章：コンテナ入門</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .section {
            background: white;
            border-radius: 8px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #1abc9c;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
        }
        .diagram-container {
            margin: 30px 0;
            text-align: center;
        }
        .command-box {
            background: #2c3e50;
            color: #27ae60;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            margin: 15px 0;
        }
        .dockerfile-box {
            background: #34495e;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            margin: 15px 0;
        }
        .explanation {
            background: #ecf0f1;
            padding: 15px;
            border-left: 4px solid #1abc9c;
            margin: 20px 0;
        }
        .key-point {
            background: #d5f4e6;
            padding: 10px 15px;
            border-radius: 4px;
            margin: 15px 0;
        }
        svg {
            max-width: 100%;
            height: auto;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        .comparison-table th, .comparison-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        .comparison-table th {
            background: #1abc9c;
            color: white;
        }
        .comparison-table tr:nth-child(even) {
            background: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="section">
        <h1>第4章：コンテナ入門</h1>
        
        <h2>4.1 仮想化とコンテナの違い</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">アパート vs カプセルホテル</text>
                
                <!-- 仮想マシン（アパート） -->
                <g transform="translate(50, 60)">
                    <text x="175" y="0" font-size="16" font-weight="bold" fill="#2c3e50">仮想マシン = アパート</text>
                    
                    <!-- 建物全体 -->
                    <rect x="50" y="20" width="250" height="400" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
                    <text x="175" y="45" text-anchor="middle" fill="white" font-size="12" font-weight="bold">物理サーバー</text>
                    
                    <!-- ハイパーバイザー -->
                    <rect x="50" y="60" width="250" height="30" fill="#34495e"/>
                    <text x="175" y="80" text-anchor="middle" fill="white" font-size="12">ハイパーバイザー（管理人）</text>
                    
                    <!-- VM1 -->
                    <rect x="60" y="100" width="110" height="100" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                    <text x="115" y="120" text-anchor="middle" fill="white" font-size="11" font-weight="bold">VM1（1号室）</text>
                    <rect x="70" y="130" width="90" height="20" fill="#2980b9"/>
                    <text x="115" y="145" text-anchor="middle" fill="white" font-size="10">ゲストOS</text>
                    <rect x="70" y="160" width="90" height="30" fill="#5dade2"/>
                    <text x="115" y="180" text-anchor="middle" fill="white" font-size="10">アプリ</text>
                    
                    <!-- VM2 -->
                    <rect x="180" y="100" width="110" height="100" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="235" y="120" text-anchor="middle" fill="white" font-size="11" font-weight="bold">VM2（2号室）</text>
                    <rect x="190" y="130" width="90" height="20" fill="#c0392b"/>
                    <text x="235" y="145" text-anchor="middle" fill="white" font-size="10">ゲストOS</text>
                    <rect x="190" y="160" width="90" height="30" fill="#ec7063"/>
                    <text x="235" y="180" text-anchor="middle" fill="white" font-size="10">アプリ</text>
                    
                    <!-- VM3 -->
                    <rect x="60" y="210" width="110" height="100" fill="#27ae60" stroke="#2c3e50" stroke-width="2"/>
                    <text x="115" y="230" text-anchor="middle" fill="white" font-size="11" font-weight="bold">VM3（3号室）</text>
                    <rect x="70" y="240" width="90" height="20" fill="#229954"/>
                    <text x="115" y="255" text-anchor="middle" fill="white" font-size="10">ゲストOS</text>
                    <rect x="70" y="270" width="90" height="30" fill="#52be80"/>
                    <text x="115" y="290" text-anchor="middle" fill="white" font-size="10">アプリ</text>
                    
                    <!-- 特徴 -->
                    <text x="175" y="340" text-anchor="middle" font-size="11" fill="white">各部屋に完全な設備</text>
                    <text x="175" y="360" text-anchor="middle" font-size="11" fill="white">（キッチン、バス、トイレ）</text>
                    <text x="175" y="380" text-anchor="middle" font-size="11" fill="white">= 各VMに完全なOS</text>
                    <text x="175" y="400" text-anchor="middle" font-size="11" fill="white">重い・起動遅い</text>
                </g>
                
                <!-- コンテナ（カプセルホテル） -->
                <g transform="translate(450, 60)">
                    <text x="175" y="0" font-size="16" font-weight="bold" fill="#2c3e50">コンテナ = カプセルホテル</text>
                    
                    <!-- 建物全体 -->
                    <rect x="50" y="20" width="250" height="400" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
                    <text x="175" y="45" text-anchor="middle" fill="white" font-size="12" font-weight="bold">物理サーバー</text>
                    
                    <!-- ホストOS -->
                    <rect x="50" y="60" width="250" height="40" fill="#34495e"/>
                    <text x="175" y="85" text-anchor="middle" fill="white" font-size="12">ホストOS（Linux）</text>
                    
                    <!-- コンテナエンジン -->
                    <rect x="50" y="100" width="250" height="30" fill="#2c3e50"/>
                    <text x="175" y="120" text-anchor="middle" fill="white" font-size="12">Docker/Podmanエンジン</text>
                    
                    <!-- コンテナ群 -->
                    <rect x="60" y="140" width="70" height="60" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                    <text x="95" y="165" text-anchor="middle" fill="white" font-size="10">コンテナ1</text>
                    <text x="95" y="185" text-anchor="middle" fill="white" font-size="10">nginx</text>
                    
                    <rect x="140" y="140" width="70" height="60" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="175" y="165" text-anchor="middle" fill="white" font-size="10">コンテナ2</text>
                    <text x="175" y="185" text-anchor="middle" fill="white" font-size="10">MySQL</text>
                    
                    <rect x="220" y="140" width="70" height="60" fill="#27ae60" stroke="#2c3e50" stroke-width="2"/>
                    <text x="255" y="165" text-anchor="middle" fill="white" font-size="10">コンテナ3</text>
                    <text x="255" y="185" text-anchor="middle" fill="white" font-size="10">Redis</text>
                    
                    <rect x="60" y="210" width="70" height="60" fill="#f39c12" stroke="#2c3e50" stroke-width="2"/>
                    <text x="95" y="235" text-anchor="middle" fill="white" font-size="10">コンテナ4</text>
                    <text x="95" y="255" text-anchor="middle" fill="white" font-size="10">Node.js</text>
                    
                    <rect x="140" y="210" width="70" height="60" fill="#9b59b6" stroke="#2c3e50" stroke-width="2"/>
                    <text x="175" y="235" text-anchor="middle" fill="white" font-size="10">コンテナ5</text>
                    <text x="175" y="255" text-anchor="middle" fill="white" font-size="10">Python</text>
                    
                    <rect x="220" y="210" width="70" height="60" fill="#1abc9c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="255" y="235" text-anchor="middle" fill="white" font-size="10">コンテナ6</text>
                    <text x="255" y="255" text-anchor="middle" fill="white" font-size="10">Java</text>
                    
                    <!-- 特徴 -->
                    <text x="175" y="300" text-anchor="middle" font-size="11" fill="white">共用設備を利用</text>
                    <text x="175" y="320" text-anchor="middle" font-size="11" fill="white">（共用シャワー、トイレ）</text>
                    <text x="175" y="340" text-anchor="middle" font-size="11" fill="white">= ホストOSを共有</text>
                    <text x="175" y="360" text-anchor="middle" font-size="11" fill="white">軽い・起動速い</text>
                    <text x="175" y="380" text-anchor="middle" font-size="11" fill="white">効率的</text>
                </g>
                
                <!-- 比較表 -->
                <g transform="translate(50, 450)">
                    <rect x="0" y="0" width="750" height="120" fill="#ecf0f1" rx="10"/>
                    <text x="20" y="25" font-size="14" font-weight="bold" fill="#2c3e50">比較まとめ</text>
                    
                    <text x="20" y="50" font-size="12" fill="#3498db">■ 仮想マシン：</text>
                    <text x="150" y="50" font-size="12">完全に独立した環境、異なるOSも実行可能、リソース消費大</text>
                    
                    <text x="20" y="75" font-size="12" fill="#e74c3c">■ コンテナ：</text>
                    <text x="150" y="75" font-size="12">OSカーネル共有、同じOS系統のみ、リソース効率的、秒単位で起動</text>
                    
                    <text x="20" y="100" font-size="12" fill="#27ae60">■ 使い分け：</text>
                    <text x="150" y="100" font-size="12">開発・マイクロサービス→コンテナ、異なるOS必要→VM</text>
                </g>
            </svg>
        </div>
        
        <h2>4.2 Dockerの基本</h2>
        
        <div class="diagram-container">
            <svg width="850" height="550" viewBox="0 0 850 550">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">Docker = 箱詰め作業</text>
                
                <!-- 箱詰めプロセス -->
                <g transform="translate(50, 60)">
                    <text x="375" y="0" font-size="16" font-weight="bold" fill="#2c3e50">アプリケーションの箱詰めプロセス</text>
                    
                    <!-- Step 1: 材料準備 -->
                    <g transform="translate(0, 30)">
                        <rect x="0" y="0" width="150" height="120" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="10"/>
                        <text x="75" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">1. 材料準備</text>
                        
                        <circle cx="40" cy="60" r="15" fill="white"/>
                        <text x="40" y="65" text-anchor="middle" font-size="10">App</text>
                        
                        <rect x="70" y="50" width="30" height="20" fill="white"/>
                        <text x="85" y="63" text-anchor="middle" font-size="8">Lib</text>
                        
                        <polygon points="110,50 125,50 117,70" fill="white"/>
                        <text x="117" y="63" text-anchor="middle" font-size="8">設定</text>
                        
                        <text x="75" y="100" text-anchor="middle" fill="white" font-size="10">アプリ・ライブラリ</text>
                        <text x="75" y="115" text-anchor="middle" fill="white" font-size="10">設定ファイル</text>
                    </g>
                    
                    <!-- Arrow -->
                    <path d="M 160 90 L 210 90" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                    
                    <!-- Step 2: Dockerfile作成 -->
                    <g transform="translate(220, 30)">
                        <rect x="0" y="0" width="150" height="120" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                        <text x="75" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">2. レシピ作成</text>
                        
                        <rect x="20" y="40" width="110" height="60" fill="white"/>
                        <text x="75" y="55" text-anchor="middle" font-size="9" font-family="monospace">FROM ubuntu</text>
                        <text x="75" y="70" text-anchor="middle" font-size="9" font-family="monospace">RUN apt install...</text>
                        <text x="75" y="85" text-anchor="middle" font-size="9" font-family="monospace">COPY app /app</text>
                        
                        <text x="75" y="115" text-anchor="middle" fill="white" font-size="10">Dockerfile</text>
                    </g>
                    
                    <!-- Arrow -->
                    <path d="M 380 90 L 430 90" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                    
                    <!-- Step 3: イメージビルド -->
                    <g transform="translate(440, 30)">
                        <rect x="0" y="0" width="150" height="120" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10"/>
                        <text x="75" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">3. 箱詰め</text>
                        
                        <rect x="30" y="40" width="90" height="50" fill="#229954" stroke="white" stroke-width="2"/>
                        <text x="75" y="65" text-anchor="middle" fill="white" font-size="12">イメージ</text>
                        <text x="75" y="80" text-anchor="middle" fill="white" font-size="10">（完成品）</text>
                        
                        <text x="75" y="110" text-anchor="middle" fill="white" font-size="10">docker build</text>
                    </g>
                    
                    <!-- Arrow -->
                    <path d="M 600 90 L 650 90" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                    
                    <!-- Step 4: コンテナ実行 -->
                    <g transform="translate(660, 30)">
                        <rect x="0" y="0" width="150" height="120" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10"/>
                        <text x="75" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">4. 開封・実行</text>
                        
                        <rect x="30" y="40" width="90" height="50" fill="#e67e22" stroke="white" stroke-width="2" stroke-dasharray="5,5"/>
                        <text x="75" y="65" text-anchor="middle" fill="white" font-size="12">コンテナ</text>
                        <text x="75" y="80" text-anchor="middle" fill="white" font-size="10">（動作中）</text>
                        
                        <text x="75" y="110" text-anchor="middle" fill="white" font-size="10">docker run</text>
                    </g>
                </g>
                
                <!-- Dockerfile例 -->
                <g transform="translate(50, 220)">
                    <text x="200" y="0" font-size="16" font-weight="bold" fill="#2c3e50">Dockerfileの例</text>
                    
                    <rect x="0" y="20" width="400" height="200" fill="#34495e" rx="10"/>
                    <text x="15" y="45" fill="#95a5a6" font-family="monospace" font-size="12"># ベースイメージを指定</text>
                    <text x="15" y="65" fill="#3498db" font-family="monospace" font-size="12">FROM</text>
                    <text x="55" y="65" fill="white" font-family="monospace" font-size="12">node:18-alpine</text>
                    
                    <text x="15" y="85" fill="#95a5a6" font-family="monospace" font-size="12"># 作業ディレクトリを設定</text>
                    <text x="15" y="105" fill="#e74c3c" font-family="monospace" font-size="12">WORKDIR</text>
                    <text x="75" y="105" fill="white" font-family="monospace" font-size="12">/app</text>
                    
                    <text x="15" y="125" fill="#95a5a6" font-family="monospace" font-size="12"># 依存関係ファイルをコピー</text>
                    <text x="15" y="145" fill="#27ae60" font-family="monospace" font-size="12">COPY</text>
                    <text x="55" y="145" fill="white" font-family="monospace" font-size="12">package*.json ./</text>
                    
                    <text x="15" y="165" fill="#95a5a6" font-family="monospace" font-size="12"># 依存関係をインストール</text>
                    <text x="15" y="185" fill="#f39c12" font-family="monospace" font-size="12">RUN</text>
                    <text x="45" y="185" fill="white" font-family="monospace" font-size="12">npm install</text>
                    
                    <text x="15" y="205" fill="#95a5a6" font-family="monospace" font-size="12"># アプリケーションコードをコピー</text>
                </g>
                
                <!-- 基本コマンド -->
                <g transform="translate(470, 220)">
                    <text x="140" y="0" font-size="16" font-weight="bold" fill="#2c3e50">基本コマンド</text>
                    
                    <rect x="0" y="20" width="330" height="200" fill="#2c3e50" rx="10"/>
                    
                    <text x="15" y="45" fill="#27ae60" font-family="monospace" font-size="11">$ docker build -t myapp .</text>
                    <text x="15" y="65" fill="#95a5a6" font-size="10">イメージをビルド</text>
                    
                    <text x="15" y="90" fill="#27ae60" font-family="monospace" font-size="11">$ docker run -d -p 80:80 myapp</text>
                    <text x="15" y="110" fill="#95a5a6" font-size="10">コンテナを起動</text>
                    
                    <text x="15" y="135" fill="#27ae60" font-family="monospace" font-size="11">$ docker ps</text>
                    <text x="15" y="155" fill="#95a5a6" font-size="10">実行中のコンテナ一覧</text>
                    
                    <text x="15" y="180" fill="#27ae60" font-family="monospace" font-size="11">$ docker stop container_id</text>
                    <text x="15" y="200" fill="#95a5a6" font-size="10">コンテナを停止</text>
                </g>
            </svg>
        </div>
        
        <h2>4.3 イメージとコンテナ</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">イメージ = 設計図、コンテナ = 製品</text>
                
                <!-- イメージとコンテナの関係 -->
                <g transform="translate(50, 60)">
                    <!-- イメージ（設計図） -->
                    <g transform="translate(0, 0)">
                        <text x="175" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">Dockerイメージ（設計図）</text>
                        
                        <rect x="50" y="20" width="250" height="200" fill="#3498db" stroke="#2c3e50" stroke-width="3" rx="10"/>
                        
                        <!-- レイヤー構造 -->
                        <rect x="70" y="40" width="210" height="30" fill="#2980b9"/>
                        <text x="175" y="60" text-anchor="middle" fill="white" font-size="12">ベースOS (Ubuntu)</text>
                        
                        <rect x="70" y="80" width="210" height="30" fill="#3498db"/>
                        <text x="175" y="100" text-anchor="middle" fill="white" font-size="12">ランタイム (Node.js)</text>
                        
                        <rect x="70" y="120" width="210" height="30" fill="#5dade2"/>
                        <text x="175" y="140" text-anchor="middle" fill="white" font-size="12">ライブラリ (npm packages)</text>
                        
                        <rect x="70" y="160" width="210" height="30" fill="#85c1e2"/>
                        <text x="175" y="180" text-anchor="middle" fill="white" font-size="12">アプリケーション</text>
                        
                        <text x="175" y="210" text-anchor="middle" fill="white" font-size="11">読み取り専用・不変</text>
                    </g>
                    
                    <!-- 矢印 -->
                    <g transform="translate(320, 100)">
                        <path d="M 0 20 L 80 20" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                        <text x="40" y="10" text-anchor="middle" font-size="12">docker run</text>
                        
                        <path d="M 0 60 L 80 60" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                        <text x="40" y="50" text-anchor="middle" font-size="12">docker run</text>
                        
                        <path d="M 0 100 L 80 100" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                        <text x="40" y="90" text-anchor="middle" font-size="12">docker run</text>
                    </g>
                    
                    <!-- コンテナ（製品） -->
                    <g transform="translate(450, 0)">
                        <text x="150" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">実行中のコンテナ（製品）</text>
                        
                        <!-- コンテナ1 -->
                        <rect x="50" y="20" width="200" height="80" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10" stroke-dasharray="5,5"/>
                        <text x="150" y="45" text-anchor="middle" fill="white" font-size="12">コンテナ1（開発環境）</text>
                        <rect x="70" y="55" width="160" height="30" fill="#c0392b" opacity="0.5"/>
                        <text x="150" y="75" text-anchor="middle" fill="white" font-size="10">書き込み可能レイヤー</text>
                        
                        <!-- コンテナ2 -->
                        <rect x="50" y="110" width="200" height="80" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10" stroke-dasharray="5,5"/>
                        <text x="150" y="135" text-anchor="middle" fill="white" font-size="12">コンテナ2（テスト環境）</text>
                        <rect x="70" y="145" width="160" height="30" fill="#229954" opacity="0.5"/>
                        <text x="150" y="165" text-anchor="middle" fill="white" font-size="10">書き込み可能レイヤー</text>
                        
                        <!-- コンテナ3 -->
                        <rect x="50" y="200" width="200" height="80" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10" stroke-dasharray="5,5"/>
                        <text x="150" y="225" text-anchor="middle" fill="white" font-size="12">コンテナ3（本番環境）</text>
                        <rect x="70" y="235" width="160" height="30" fill="#e67e22" opacity="0.5"/>
                        <text x="150" y="255" text-anchor="middle" fill="white" font-size="10">書き込み可能レイヤー</text>
                    </g>
                </g>
                
                <!-- ライフサイクル -->
                <g transform="translate(50, 350)">
                    <text x="375" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">コンテナのライフサイクル</text>
                    
                    <rect x="0" y="20" width="750" height="200" fill="#ecf0f1" rx="10"/>
                    
                    <!-- Create -->
                    <circle cx="100" cy="100" r="40" fill="#95a5a6"/>
                    <text x="100" y="105" text-anchor="middle" fill="white" font-size="12">作成</text>
                    <text x="100" y="155" text-anchor="middle" font-size="10">docker create</text>
                    
                    <!-- Start -->
                    <circle cx="250" cy="100" r="40" fill="#3498db"/>
                    <text x="250" y="105" text-anchor="middle" fill="white" font-size="12">起動</text>
                    <text x="250" y="155" text-anchor="middle" font-size="10">docker start</text>
                    
                    <!-- Running -->
                    <circle cx="400" cy="100" r="40" fill="#27ae60"/>
                    <text x="400" y="105" text-anchor="middle" fill="white" font-size="12">実行中</text>
                    <text x="400" y="155" text-anchor="middle" font-size="10">docker ps</text>
                    
                    <!-- Stop -->
                    <circle cx="550" cy="100" r="40" fill="#f39c12"/>
                    <text x="550" y="105" text-anchor="middle" fill="white" font-size="12">停止</text>
                    <text x="550" y="155" text-anchor="middle" font-size="10">docker stop</text>
                    
                    <!-- Remove -->
                    <circle cx="700" cy="100" r="40" fill="#e74c3c"/>
                    <text x="700" y="105" text-anchor="middle" fill="white" font-size="12">削除</text>
                    <text x="700" y="155" text-anchor="middle" font-size="10">docker rm</text>
                    
                    <!-- 矢印 -->
                    <path d="M 140 100 L 210 100" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <path d="M 290 100 L 360 100" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <path d="M 440 100 L 510 100" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <path d="M 590 100 L 660 100" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    
                    <!-- Restart loop -->
                    <path d="M 550 60 Q 400 20 250 60" stroke="#7f8c8d" stroke-width="1" stroke-dasharray="3,3" fill="none" marker-end="url(#arrowhead)"/>
                    <text x="400" y="35" text-anchor="middle" font-size="10" fill="#7f8c8d">restart</text>
                </g>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>重要な概念：</strong>
            <ul>
                <li><strong>イメージ：</strong>読み取り専用のテンプレート。何度でも同じコンテナを作成可能</li>
                <li><strong>コンテナ：</strong>イメージから作成された実行インスタンス。独立した実行環境</li>
                <li><strong>レイヤー：</strong>イメージは複数のレイヤーで構成。効率的な共有と保存</li>
                <li><strong>レジストリ：</strong>イメージの保管場所（Docker Hub、ECR、GCR等）</li>
            </ul>
        </div>
        
        <div class="key-point">
            <strong>Docker vs Podman：</strong>
            <ul style="margin: 5px 0;">
                <li>Docker: デーモン型、root権限必要な場合あり</li>
                <li>Podman: デーモンレス、rootless実行可能、Dockerコマンド互換</li>
            </ul>
        </div>
        
        <div class="command-box">
# イメージ管理<br>
$ docker images                    # イメージ一覧<br>
$ docker pull nginx:latest         # イメージ取得<br>
$ docker rmi image_id              # イメージ削除<br><br>

# コンテナ管理<br>
$ docker run -it ubuntu /bin/bash  # インタラクティブ実行<br>
$ docker exec -it container_id bash # 実行中のコンテナに接続<br>
$ docker logs container_id         # ログ確認<br>
$ docker inspect container_id      # 詳細情報確認
        </div>
    </div>
</body>
</html>