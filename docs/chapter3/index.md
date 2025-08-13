---
layout: chapter
title: "第3章：ネットワークの基礎"
chapter: 3
---
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第3章：ネットワークの基礎</title>
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
            border-bottom: 3px solid #9b59b6;
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
        .explanation {
            background: #ecf0f1;
            padding: 15px;
            border-left: 4px solid #9b59b6;
            margin: 20px 0;
        }
        .key-point {
            background: #f4ecf7;
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
        .network-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        .network-table th, .network-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        .network-table th {
            background: #9b59b6;
            color: white;
        }
        .network-table tr:nth-child(even) {
            background: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="section">
        <h1>第3章：ネットワークの基礎</h1>
        
        <h2>3.1 IPアドレスとは</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">IPアドレス = インターネット上の住所</text>
                
                <!-- 住所システムとの対比 -->
                <g transform="translate(50, 60)">
                    <text x="200" y="0" font-size="16" font-weight="bold" fill="#2c3e50">現実世界の住所</text>
                    
                    <!-- 家のイメージ -->
                    <rect x="100" y="20" width="200" height="150" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <polygon points="100,20 200,0 300,20" fill="#c0392b" stroke="#2c3e50" stroke-width="2"/>
                    <rect x="170" y="80" width="60" height="90" fill="#8b6f47" stroke="#2c3e50" stroke-width="2"/>
                    <circle cx="215" cy="125" r="3" fill="#f39c12"/>
                    
                    <!-- 住所表記 -->
                    <rect x="80" y="190" width="240" height="80" fill="#f8f9fa" stroke="#34495e" stroke-width="2" rx="5"/>
                    <text x="200" y="215" text-anchor="middle" font-size="14" font-weight="bold">〒100-0001</text>
                    <text x="200" y="235" text-anchor="middle" font-size="12">東京都千代田区</text>
                    <text x="200" y="255" text-anchor="middle" font-size="12">千代田1-1-1</text>
                </g>
                
                <!-- IPアドレス -->
                <g transform="translate(450, 60)">
                    <text x="175" y="0" font-size="16" font-weight="bold" fill="#2c3e50">ネットワークの住所</text>
                    
                    <!-- サーバーのイメージ -->
                    <rect x="100" y="20" width="150" height="150" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                    <rect x="115" y="40" width="120" height="15" fill="#2c3e50"/>
                    <circle cx="125" cy="47" r="3" fill="#27ae60"/>
                    <circle cx="135" cy="47" r="3" fill="#f39c12"/>
                    
                    <rect x="115" y="70" width="120" height="15" fill="#2c3e50"/>
                    <circle cx="125" cy="77" r="3" fill="#27ae60"/>
                    <circle cx="135" cy="77" r="3" fill="#e74c3c"/>
                    
                    <rect x="115" y="100" width="120" height="15" fill="#2c3e50"/>
                    <circle cx="125" cy="107" r="3" fill="#27ae60"/>
                    <circle cx="135" cy="107" r="3" fill="#f39c12"/>
                    
                    <!-- IPアドレス表記 -->
                    <rect x="75" y="190" width="200" height="80" fill="#f8f9fa" stroke="#34495e" stroke-width="2" rx="5"/>
                    <text x="175" y="220" text-anchor="middle" font-size="18" font-weight="bold" font-family="monospace">192.168.1.100</text>
                    <text x="175" y="245" text-anchor="middle" font-size="10" fill="#7f8c8d">ネットワーク部 | ホスト部</text>
                    <text x="175" y="260" text-anchor="middle" font-size="10" fill="#7f8c8d">192.168.1    |    100</text>
                </g>
                
                <!-- IPv4の構造 -->
                <g transform="translate(50, 320)">
                    <text x="375" y="0" text-anchor="middle" font-size="18" font-weight="bold" fill="#2c3e50">IPv4アドレスの構造</text>
                    
                    <!-- 4つのオクテット -->
                    <rect x="200" y="30" width="80" height="60" fill="#3498db" rx="10"/>
                    <text x="240" y="65" text-anchor="middle" fill="white" font-size="20" font-weight="bold">192</text>
                    <text x="240" y="110" text-anchor="middle" font-size="10">第1オクテット</text>
                    
                    <rect x="290" y="30" width="80" height="60" fill="#e74c3c" rx="10"/>
                    <text x="330" y="65" text-anchor="middle" fill="white" font-size="20" font-weight="bold">168</text>
                    <text x="330" y="110" text-anchor="middle" font-size="10">第2オクテット</text>
                    
                    <rect x="380" y="30" width="80" height="60" fill="#27ae60" rx="10"/>
                    <text x="420" y="65" text-anchor="middle" fill="white" font-size="20" font-weight="bold">1</text>
                    <text x="420" y="110" text-anchor="middle" font-size="10">第3オクテット</text>
                    
                    <rect x="470" y="30" width="80" height="60" fill="#f39c12" rx="10"/>
                    <text x="510" y="65" text-anchor="middle" fill="white" font-size="20" font-weight="bold">100</text>
                    <text x="510" y="110" text-anchor="middle" font-size="10">第4オクテット</text>
                    
                    <!-- ドット -->
                    <circle cx="285" cy="60" r="3" fill="#2c3e50"/>
                    <circle cx="375" cy="60" r="3" fill="#2c3e50"/>
                    <circle cx="465" cy="60" r="3" fill="#2c3e50"/>
                    
                    <!-- 範囲説明 -->
                    <text x="375" y="140" text-anchor="middle" font-size="12" fill="#7f8c8d">各オクテット: 0～255（8ビット = 256通り）</text>
                </g>
                
                <!-- 特殊なIPアドレス -->
                <g transform="translate(50, 470)">
                    <rect x="0" y="0" width="750" height="100" fill="#ecf0f1" rx="10"/>
                    <text x="20" y="25" font-size="14" font-weight="bold" fill="#2c3e50">よく使うIPアドレス</text>
                    
                    <text x="20" y="50" font-family="monospace" font-size="12" fill="#3498db">127.0.0.1</text>
                    <text x="120" y="50" font-size="12">= localhost（自分自身）</text>
                    
                    <text x="20" y="70" font-family="monospace" font-size="12" fill="#e74c3c">192.168.x.x</text>
                    <text x="120" y="70" font-size="12">= プライベートIPアドレス（LAN内）</text>
                    
                    <text x="20" y="90" font-family="monospace" font-size="12" fill="#27ae60">0.0.0.0</text>
                    <text x="120" y="90" font-size="12">= すべてのインターフェース</text>
                    
                    <text x="400" y="50" font-family="monospace" font-size="12" fill="#9b59b6">10.x.x.x</text>
                    <text x="500" y="50" font-size="12">= プライベートIPアドレス（大規模）</text>
                    
                    <text x="400" y="70" font-family="monospace" font-size="12" fill="#f39c12">8.8.8.8</text>
                    <text x="500" y="70" font-size="12">= Google Public DNS</text>
                </g>
            </svg>
        </div>
        
        <div class="key-point">
            <strong>IPv4 vs IPv6：</strong>
            <ul style="margin: 5px 0;">
                <li>IPv4: 32ビット（約43億個）例: 192.168.1.1</li>
                <li>IPv6: 128ビット（ほぼ無限）例: 2001:0db8:0000:0000:0000:8a2e:0370:7334</li>
            </ul>
        </div>
        
        <h2>3.2 ポートの概念</h2>
        
        <div class="diagram-container">
            <svg width="850" height="550" viewBox="0 0 850 550">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ポート = マンションの部屋番号</text>
                
                <!-- マンションのアナロジー -->
                <g transform="translate(100, 60)">
                    <text x="175" y="0" font-size="16" font-weight="bold" fill="#2c3e50">マンションに例えると...</text>
                    
                    <!-- マンション建物 -->
                    <rect x="50" y="20" width="250" height="300" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
                    <text x="175" y="45" text-anchor="middle" fill="white" font-size="14" font-weight="bold">IPアドレス: 192.168.1.100</text>
                    <text x="175" y="65" text-anchor="middle" fill="white" font-size="12">（建物の住所）</text>
                    
                    <!-- 各部屋（ポート） -->
                    <!-- 80番 -->
                    <rect x="70" y="90" width="90" height="50" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                    <text x="115" y="110" text-anchor="middle" fill="white" font-size="14" font-weight="bold">80号室</text>
                    <text x="115" y="130" text-anchor="middle" fill="white" font-size="10">HTTP</text>
                    
                    <!-- 443番 -->
                    <rect x="190" y="90" width="90" height="50" fill="#27ae60" stroke="#2c3e50" stroke-width="2"/>
                    <text x="235" y="110" text-anchor="middle" fill="white" font-size="14" font-weight="bold">443号室</text>
                    <text x="235" y="130" text-anchor="middle" fill="white" font-size="10">HTTPS</text>
                    
                    <!-- 22番 -->
                    <rect x="70" y="160" width="90" height="50" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="115" y="180" text-anchor="middle" fill="white" font-size="14" font-weight="bold">22号室</text>
                    <text x="115" y="200" text-anchor="middle" fill="white" font-size="10">SSH</text>
                    
                    <!-- 3306番 -->
                    <rect x="190" y="160" width="90" height="50" fill="#f39c12" stroke="#2c3e50" stroke-width="2"/>
                    <text x="235" y="180" text-anchor="middle" fill="white" font-size="14" font-weight="bold">3306号室</text>
                    <text x="235" y="200" text-anchor="middle" fill="white" font-size="10">MySQL</text>
                    
                    <!-- 25番 -->
                    <rect x="70" y="230" width="90" height="50" fill="#9b59b6" stroke="#2c3e50" stroke-width="2"/>
                    <text x="115" y="250" text-anchor="middle" fill="white" font-size="14" font-weight="bold">25号室</text>
                    <text x="115" y="270" text-anchor="middle" fill="white" font-size="10">SMTP</text>
                    
                    <!-- 21番 -->
                    <rect x="190" y="230" width="90" height="50" fill="#1abc9c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="235" y="250" text-anchor="middle" fill="white" font-size="14" font-weight="bold">21号室</text>
                    <text x="235" y="270" text-anchor="middle" fill="white" font-size="10">FTP</text>
                </g>
                
                <!-- よく使うポート番号 -->
                <g transform="translate(450, 80)">
                    <text x="150" y="0" font-size="16" font-weight="bold" fill="#2c3e50">主要なポート番号</text>
                    
                    <rect x="0" y="20" width="300" height="260" fill="#f8f9fa" stroke="#34495e" stroke-width="2" rx="10"/>
                    
                    <!-- Well-known ports -->
                    <text x="15" y="45" font-size="14" font-weight="bold" fill="#2c3e50">■ Well-known（0-1023）</text>
                    <text x="25" y="70" font-size="12"><tspan fill="#e74c3c" font-weight="bold">22</tspan> - SSH（セキュアシェル）</text>
                    <text x="25" y="90" font-size="12"><tspan fill="#3498db" font-weight="bold">80</tspan> - HTTP（Web）</text>
                    <text x="25" y="110" font-size="12"><tspan fill="#27ae60" font-weight="bold">443</tspan> - HTTPS（暗号化Web）</text>
                    <text x="25" y="130" font-size="12"><tspan fill="#9b59b6" font-weight="bold">25</tspan> - SMTP（メール送信）</text>
                    
                    <!-- Registered ports -->
                    <text x="15" y="160" font-size="14" font-weight="bold" fill="#2c3e50">■ Registered（1024-49151）</text>
                    <text x="25" y="185" font-size="12"><tspan fill="#f39c12" font-weight="bold">3306</tspan> - MySQL</text>
                    <text x="25" y="205" font-size="12"><tspan fill="#e67e22" font-weight="bold">5432</tspan> - PostgreSQL</text>
                    <text x="25" y="225" font-size="12"><tspan fill="#d35400" font-weight="bold">6379</tspan> - Redis</text>
                    <text x="25" y="245" font-size="12"><tspan fill="#c0392b" font-weight="bold">8080</tspan> - 代替HTTP</text>
                    
                    <!-- Dynamic ports -->
                    <text x="15" y="270" font-size="12" fill="#7f8c8d">■ Dynamic（49152-65535）: 一時利用</text>
                </g>
                
                <!-- 接続の流れ -->
                <g transform="translate(50, 380)">
                    <text x="375" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">接続の流れ</text>
                    
                    <rect x="0" y="20" width="750" height="120" fill="#2c3e50" rx="10"/>
                    
                    <!-- クライアント -->
                    <rect x="20" y="40" width="150" height="60" fill="#3498db" rx="5"/>
                    <text x="95" y="65" text-anchor="middle" fill="white" font-size="12">クライアント</text>
                    <text x="95" y="85" text-anchor="middle" fill="white" font-size="10">192.168.1.10:54321</text>
                    
                    <!-- 矢印 -->
                    <path d="M 180 70 L 280 70" stroke="white" stroke-width="2" marker-end="url(#arrowhead-white)"/>
                    <text x="230" y="60" text-anchor="middle" fill="white" font-size="10">接続要求</text>
                    
                    <!-- サーバー -->
                    <rect x="290" y="40" width="150" height="60" fill="#e74c3c" rx="5"/>
                    <text x="365" y="65" text-anchor="middle" fill="white" font-size="12">Webサーバー</text>
                    <text x="365" y="85" text-anchor="middle" fill="white" font-size="10">192.168.1.100:80</text>
                    
                    <!-- レスポンス -->
                    <path d="M 440 90 L 540 90" stroke="white" stroke-width="2" stroke-dasharray="5,5"/>
                    <text x="490" y="80" text-anchor="middle" fill="white" font-size="10">応答</text>
                    
                    <!-- 説明 -->
                    <text x="580" y="70" fill="white" font-size="11">「192.168.1.100の80番ポートに</text>
                    <text x="580" y="90" fill="white" font-size="11">　接続したい」という要求</text>
                    
                    <defs>
                        <marker id="arrowhead-white" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                            <polygon points="0 0, 10 3.5, 0 7" fill="white"/>
                        </marker>
                    </defs>
                </g>
            </svg>
        </div>
        
        <div class="command-box">
$ netstat -tuln    # 開いているポートを確認<br>
$ ss -tuln         # 新しいコマンド（netstatの代替）<br>
$ lsof -i :80      # 80番ポートを使用しているプロセスを確認
        </div>
        
        <h2>3.3 通信の流れ</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ネットワーク通信 = 郵便配達</text>
                
                <!-- OSI参照モデル風の層 -->
                <g transform="translate(50, 60)">
                    <text x="200" y="0" font-size="16" font-weight="bold" fill="#2c3e50">データの梱包と配送</text>
                    
                    <!-- アプリケーション層 -->
                    <rect x="50" y="30" width="300" height="50" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                    <text x="200" y="60" text-anchor="middle" fill="white" font-size="14" font-weight="bold">アプリケーション層</text>
                    <text x="380" y="60" font-size="12">手紙の内容（HTTPリクエスト等）</text>
                    
                    <!-- トランスポート層 -->
                    <rect x="50" y="90" width="300" height="50" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="200" y="120" text-anchor="middle" fill="white" font-size="14" font-weight="bold">トランスポート層（TCP/UDP）</text>
                    <text x="380" y="120" font-size="12">封筒に入れる（ポート番号付与）</text>
                    
                    <!-- ネットワーク層 -->
                    <rect x="50" y="150" width="300" height="50" fill="#27ae60" stroke="#2c3e50" stroke-width="2"/>
                    <text x="200" y="180" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ネットワーク層（IP）</text>
                    <text x="380" y="180" font-size="12">宛先住所を書く（IPアドレス）</text>
                    
                    <!-- データリンク層 -->
                    <rect x="50" y="210" width="300" height="50" fill="#f39c12" stroke="#2c3e50" stroke-width="2"/>
                    <text x="200" y="240" text-anchor="middle" fill="white" font-size="14" font-weight="bold">データリンク層</text>
                    <text x="380" y="240" font-size="12">配送トラックに載せる（MACアドレス）</text>
                    
                    <!-- 物理層 -->
                    <rect x="50" y="270" width="300" height="50" fill="#9b59b6" stroke="#2c3e50" stroke-width="2"/>
                    <text x="200" y="300" text-anchor="middle" fill="white" font-size="14" font-weight="bold">物理層</text>
                    <text x="380" y="300" font-size="12">実際の配送（電気信号・光信号）</text>
                </g>
                
                <!-- 実際の通信フロー -->
                <g transform="translate(50, 400)">
                    <text x="375" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">Webページアクセスの流れ</text>
                    
                    <!-- PC -->
                    <rect x="50" y="30" width="80" height="60" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                    <text x="90" y="60" text-anchor="middle" fill="white" font-size="12">あなたのPC</text>
                    <text x="90" y="110" text-anchor="middle" font-size="10">192.168.1.10</text>
                    
                    <!-- Step 1: DNS -->
                    <path d="M 140 60 L 210 60" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="175" y="50" text-anchor="middle" font-size="10">①DNS問合せ</text>
                    
                    <rect x="220" y="30" width="80" height="60" fill="#1abc9c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="260" y="55" text-anchor="middle" fill="white" font-size="12">DNSサーバー</text>
                    <text x="260" y="75" text-anchor="middle" fill="white" font-size="10">名前→IP変換</text>
                    
                    <!-- Step 2: ルーター -->
                    <path d="M 140 90 L 350 90" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="245" y="105" text-anchor="middle" font-size="10">②ルーティング</text>
                    
                    <rect x="360" y="30" width="80" height="60" fill="#e67e22" stroke="#2c3e50" stroke-width="2"/>
                    <text x="400" y="55" text-anchor="middle" fill="white" font-size="12">ルーター</text>
                    <text x="400" y="75" text-anchor="middle" fill="white" font-size="10">経路選択</text>
                    
                    <!-- Step 3: インターネット -->
                    <path d="M 450 60 L 520 60" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="485" y="50" text-anchor="middle" font-size="10">③インターネット</text>
                    
                    <ellipse cx="570" cy="60" rx="40" ry="30" fill="#95a5a6" stroke="#2c3e50" stroke-width="2"/>
                    <text x="570" y="65" text-anchor="middle" fill="white" font-size="12">Internet</text>
                    
                    <!-- Step 4: Webサーバー -->
                    <path d="M 620 60 L 680 60" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="650" y="50" text-anchor="middle" font-size="10">④到達</text>
                    
                    <rect x="690" y="30" width="80" height="60" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="730" y="55" text-anchor="middle" fill="white" font-size="12">Webサーバー</text>
                    <text x="730" y="75" text-anchor="middle" fill="white" font-size="10">203.0.113.1</text>
                    
                    <!-- レスポンス -->
                    <path d="M 730 90 L 90 120" stroke="#27ae60" stroke-width="2" stroke-dasharray="5,5"/>
                    <text x="410" y="140" text-anchor="middle" font-size="10" fill="#27ae60">⑤レスポンス（Webページ）</text>
                </g>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>ネットワーク診断コマンド：</strong>
            <ul>
                <li><code>ping</code> - 接続確認（例: ping google.com）</li>
                <li><code>traceroute</code> - 経路確認（例: traceroute google.com）</li>
                <li><code>nslookup</code> / <code>dig</code> - DNS確認</li>
                <li><code>curl</code> / <code>wget</code> - HTTPリクエスト送信</li>
                <li><code>ip addr</code> / <code>ifconfig</code> - ネットワークインターフェース確認</li>
                <li><code>netstat</code> / <code>ss</code> - ネットワーク接続状態確認</li>
            </ul>
        </div>
        
        <div class="key-point">
            <strong>TCP vs UDP：</strong>
            <ul style="margin: 5px 0;">
                <li><strong>TCP：</strong>信頼性重視。確実にデータ到達（Web、メール、ファイル転送）</li>
                <li><strong>UDP：</strong>速度重視。多少のロスOK（動画ストリーミング、オンラインゲーム、DNS）</li>
            </ul>
        </div>
    </div>
</body>
</html>