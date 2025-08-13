---
layout: chapter
title: "第4章：コンテナ入門"
chapter: 4
---

<div class="section">
    <h1>第4章：コンテナ入門</h1>
    
    <h2>4.1 仮想化とコンテナの違い</h2>
    
    <div class="diagram-container">
        <svg width="850" height="600" viewBox="0 0 850 600">
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
                <text x="115" y="120" text-anchor="middle" fill="white" font-size="11" font-weight="bold">VM1</text>
                <rect x="70" y="130" width="90" height="20" fill="#2980b9"/>
                <text x="115" y="145" text-anchor="middle" fill="white" font-size="10">ゲストOS</text>
                <rect x="70" y="160" width="90" height="30" fill="#5dade2"/>
                <text x="115" y="180" text-anchor="middle" fill="white" font-size="10">アプリ</text>
                
                <!-- VM2 -->
                <rect x="180" y="100" width="110" height="100" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                <text x="235" y="120" text-anchor="middle" fill="white" font-size="11" font-weight="bold">VM2</text>
                <rect x="190" y="130" width="90" height="20" fill="#c0392b"/>
                <text x="235" y="145" text-anchor="middle" fill="white" font-size="10">ゲストOS</text>
                <rect x="190" y="160" width="90" height="30" fill="#ec7063"/>
                <text x="235" y="180" text-anchor="middle" fill="white" font-size="10">アプリ</text>
            </g>
            
            <!-- コンテナ（カプセルホテル） -->
            <g transform="translate(450, 60)">
                <text x="175" y="0" font-size="16" font-weight="bold" fill="#2c3e50">コンテナ = カプセルホテル</text>
                
                <rect x="50" y="20" width="250" height="400" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
                <text x="175" y="45" text-anchor="middle" fill="white" font-size="12" font-weight="bold">物理サーバー</text>
                
                <!-- ホストOS -->
                <rect x="50" y="60" width="250" height="40" fill="#34495e"/>
                <text x="175" y="85" text-anchor="middle" fill="white" font-size="12">ホストOS + Docker Engine</text>
                
                <!-- コンテナ群 -->
                <rect x="60" y="110" width="70" height="60" fill="#f39c12" stroke="#2c3e50"/>
                <text x="95" y="135" text-anchor="middle" fill="white" font-size="10">App1</text>
                
                <rect x="140" y="110" width="70" height="60" fill="#9b59b6" stroke="#2c3e50"/>
                <text x="175" y="135" text-anchor="middle" fill="white" font-size="10">App2</text>
                
                <rect x="220" y="110" width="70" height="60" fill="#1abc9c" stroke="#2c3e50"/>
                <text x="255" y="135" text-anchor="middle" fill="white" font-size="10">App3</text>
            </g>
            
            <!-- 比較 -->
            <g transform="translate(50, 480)">
                <rect x="0" y="0" width="750" height="100" fill="#ecf0f1" rx="10"/>
                <text x="20" y="25" font-size="14" font-weight="bold" fill="#2c3e50">主な違い</text>
                
                <text x="20" y="50" font-size="12" fill="#3498db">・仮想マシン: 各VMが完全なOSを持つ（重い）</text>
                <text x="20" y="70" font-size="12" fill="#f39c12">・コンテナ: OSカーネルを共有（軽い）</text>
                <text x="20" y="90" font-size="12" fill="#27ae60">・コンテナは秒で起動、VMは分単位</text>
                
                <text x="400" y="50" font-size="12" fill="#e74c3c">・仮想マシン: 完全に隔離（セキュア）</text>
                <text x="400" y="70" font-size="12" fill="#9b59b6">・コンテナ: プロセスレベルの隔離</text>
                <text x="400" y="90" font-size="12" fill="#1abc9c">・コンテナはリソース効率が良い</text>
            </g>
        </svg>
    </div>
    
    <h2>4.2 Dockerの基本概念</h2>
    
    <div class="container-concept">
        <h3>Docker = アプリの引っ越し業者</h3>
        <p>Dockerは「アプリケーションとその環境をまとめて梱包」して、どこでも同じように動かせるツールです。</p>
    </div>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>docker run - コンテナ実行</h3>
            <div class="command-box">$ docker run hello-world</div>
            <p>最初のテスト用コンテナを実行</p>
        </div>
        
        <div class="command-card">
            <h3>docker ps - コンテナ一覧</h3>
            <div class="command-box">$ docker ps -a</div>
            <p>実行中・停止中のコンテナを表示</p>
        </div>
        
        <div class="command-card">
            <h3>docker images - イメージ一覧</h3>
            <div class="command-box">$ docker images</div>
            <p>ダウンロードしたイメージを表示</p>
        </div>
        
        <div class="command-card">
            <h3>docker pull - イメージ取得</h3>
            <div class="command-box">$ docker pull ubuntu</div>
            <p>Docker Hubからイメージをダウンロード</p>
        </div>
    </div>
    
    <h2>4.3 実際にDockerを使ってみよう</h2>
    
    <div class="practice-step">
        <h4>ステップ1: Webサーバーを起動</h4>
        <div class="command-box">$ docker run -p 8080:80 nginx</div>
        <p>ブラウザで http://localhost:8080 にアクセスしてみましょう</p>
    </div>
    
    <div class="practice-step">
        <h4>ステップ2: バックグラウンド実行</h4>
        <div class="command-box">$ docker run -d -p 8080:80 --name my-nginx nginx</div>
        <p><code>-d</code>でバックグラウンド実行、<code>--name</code>で名前を付ける</p>
    </div>
    
    <div class="practice-step">
        <h4>ステップ3: コンテナ操作</h4>
        <div class="command-box">$ docker stop my-nginx</div>
        <div class="command-box">$ docker start my-nginx</div>
        <div class="command-box">$ docker rm my-nginx</div>
        <p>コンテナの停止・開始・削除</p>
    </div>
    
    <div class="key-point">
        <strong>覚えておこう：</strong>
        <ul>
            <li><strong>Image</strong> - アプリの設計図（テンプレート）</li>
            <li><strong>Container</strong> - Imageから作られた実行中のアプリ</li>
            <li><strong>Port mapping</strong> - ホストとコンテナのポート接続</li>
            <li><strong>Docker Hub</strong> - イメージの公開リポジトリ</li>
        </ul>
    </div>
</div>