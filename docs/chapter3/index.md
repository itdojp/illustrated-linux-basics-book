---
layout: chapter
title: "第3章：ネットワークの基礎"
chapter: 3
---

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
                    
                    <text x="400" y="70" font-family="monospace" font-size="12" fill="#1abc9c">172.16.x.x</text>
                    <text x="500" y="70" font-size="12">= プライベートIPアドレス（中規模）</text>
                </g>
            </svg>
        </div>
        
        <div class="key-point">
            <strong>覚えておこう：</strong>
            <ul style="margin: 5px 0;">
                <li><strong>127.0.0.1</strong> - 自分自身を指す特別なアドレス</li>
                <li><strong>192.168.x.x</strong> - 家庭やオフィスのLAN内で使用</li>
                <li><strong>グローバルIP</strong> - インターネット上で使用される固有アドレス</li>
                <li><strong>プライベートIP</strong> - LAN内でのみ使用される内部アドレス</li>
            </ul>
        </div>
        
        <h2>3.2 ポートとは</h2>
        
        <div class="diagram-container">
            <svg width="800" height="500" viewBox="0 0 800 500">
                <!-- タイトル -->
                <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ポート = サービスの窓口</text>
                
                <!-- マンションの例え -->
                <g transform="translate(100, 60)">
                    <text x="200" y="0" font-size="16" font-weight="bold" fill="#2c3e50">マンションに例えると...</text>
                    
                    <!-- ビル -->
                    <rect x="150" y="30" width="100" height="200" fill="#34495e" stroke="#2c3e50" stroke-width="2"/>
                    
                    <!-- 部屋 -->
                    <rect x="160" y="50" width="35" height="30" fill="#3498db" stroke="#2c3e50"/>
                    <text x="177" y="70" text-anchor="middle" fill="white" font-size="10">101</text>
                    <text x="177" y="95" text-anchor="middle" font-size="8" fill="#7f8c8d">Web</text>
                    
                    <rect x="205" y="50" width="35" height="30" fill="#e74c3c" stroke="#2c3e50"/>
                    <text x="222" y="70" text-anchor="middle" fill="white" font-size="10">102</text>
                    <text x="222" y="95" text-anchor="middle" font-size="8" fill="#7f8c8d">Mail</text>
                    
                    <rect x="160" y="110" width="35" height="30" fill="#27ae60" stroke="#2c3e50"/>
                    <text x="177" y="130" text-anchor="middle" fill="white" font-size="10">201</text>
                    <text x="177" y="155" text-anchor="middle" font-size="8" fill="#7f8c8d">SSH</text>
                    
                    <rect x="205" y="110" width="35" height="30" fill="#f39c12" stroke="#2c3e50"/>
                    <text x="222" y="130" text-anchor="middle" fill="white" font-size="10">202</text>
                    <text x="222" y="155" text-anchor="middle" font-size="8" fill="#7f8c8d">FTP</text>
                    
                    <!-- 住所プレート -->
                    <rect x="120" y="250" width="160" height="40" fill="#f8f9fa" stroke="#34495e" stroke-width="2" rx="5"/>
                    <text x="200" y="275" text-anchor="middle" font-size="14" font-weight="bold">192.168.1.10</text>
                    <text x="200" y="285" text-anchor="middle" font-size="8" fill="#7f8c8d">（マンション全体の住所）</text>
                </g>
                
                <!-- サーバーの実例 -->
                <g transform="translate(450, 60)">
                    <text x="150" y="0" font-size="16" font-weight="bold" fill="#2c3e50">サーバーの実例</text>
                    
                    <!-- サーバー -->
                    <rect x="100" y="30" width="100" height="200" fill="#2c3e50" stroke="#34495e" stroke-width="2"/>
                    
                    <!-- サービス -->
                    <rect x="110" y="50" width="80" height="25" fill="#3498db"/>
                    <text x="150" y="67" text-anchor="middle" fill="white" font-size="10">HTTP: 80</text>
                    
                    <rect x="110" y="85" width="80" height="25" fill="#27ae60"/>
                    <text x="150" y="102" text-anchor="middle" fill="white" font-size="10">HTTPS: 443</text>
                    
                    <rect x="110" y="120" width="80" height="25" fill="#e74c3c"/>
                    <text x="150" y="137" text-anchor="middle" fill="white" font-size="10">SSH: 22</text>
                    
                    <rect x="110" y="155" width="80" height="25" fill="#f39c12"/>
                    <text x="150" y="172" text-anchor="middle" fill="white" font-size="10">MySQL: 3306</text>
                    
                    <rect x="110" y="190" width="80" height="25" fill="#9b59b6"/>
                    <text x="150" y="207" text-anchor="middle" fill="white" font-size="10">DNS: 53</text>
                    
                    <!-- IPアドレス -->
                    <rect x="70" y="250" width="160" height="40" fill="#f8f9fa" stroke="#34495e" stroke-width="2" rx="5"/>
                    <text x="150" y="275" text-anchor="middle" font-size="14" font-weight="bold">192.168.1.100</text>
                    <text x="150" y="285" text-anchor="middle" font-size="8" fill="#7f8c8d">（サーバーのIPアドレス）</text>
                </g>
                
                <!-- アクセス例 -->
                <g transform="translate(100, 350)">
                    <text x="300" y="0" font-size="16" font-weight="bold" fill="#2c3e50">アクセスの仕方</text>
                    
                    <rect x="50" y="20" width="500" height="100" fill="#2c3e50" stroke="#34495e" stroke-width="2"/>
                    
                    <text x="70" y="45" fill="#27ae60" font-family="monospace" font-size="12">$ ssh user@192.168.1.100</text>
                    <text x="450" y="45" fill="#7f8c8d" font-size="10">（ポート22で接続）</text>
                    
                    <text x="70" y="65" fill="#27ae60" font-family="monospace" font-size="12">$ curl http://192.168.1.100:80</text>
                    <text x="450" y="65" fill="#7f8c8d" font-size="10">（ポート80を明示）</text>
                    
                    <text x="70" y="85" fill="#27ae60" font-family="monospace" font-size="12">$ mysql -h 192.168.1.100 -P 3306</text>
                    <text x="450" y="85" fill="#7f8c8d" font-size="10">（ポート3306で接続）</text>
                    
                    <text x="70" y="105" fill="#27ae60" font-family="monospace" font-size="12">$ nc -l 8080</text>
                    <text x="450" y="105" fill="#7f8c8d" font-size="10">（ポート8080で待機）</text>
                </g>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>よく使われるポート番号：</strong>
            <ul>
                <li><strong>80</strong> - HTTP（Webサイト）</li>
                <li><strong>443</strong> - HTTPS（暗号化されたWebサイト）</li>
                <li><strong>22</strong> - SSH（安全なリモート接続）</li>
                <li><strong>25</strong> - SMTP（メール送信）</li>
                <li><strong>53</strong> - DNS（ドメイン名解決）</li>
                <li><strong>3306</strong> - MySQL（データベース）</li>
            </ul>
        </div>
        
        <h2>3.3 基本的なネットワークコマンド</h2>
        
        <div class="diagram-container">
            <svg width="850" height="550" viewBox="0 0 850 550">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ネットワーク診断ツール</text>
                
                <!-- ping -->
                <g transform="translate(50, 60)">
                    <rect x="0" y="0" width="180" height="100" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">ping</text>
                    <text x="90" y="50" text-anchor="middle" fill="white" font-size="12">疎通確認</text>
                    <text x="90" y="70" text-anchor="middle" fill="white" font-size="10">相手が応答するかチェック</text>
                    
                    <!-- ping の流れ -->
                    <circle cx="270" cy="50" r="20" fill="#ecf0f1"/>
                    <text x="270" y="55" text-anchor="middle" font-size="12">PC</text>
                    
                    <circle cx="450" cy="50" r="20" fill="#e74c3c"/>
                    <text x="450" y="55" text-anchor="middle" font-size="12">Server</text>
                    
                    <!-- 矢印 -->
                    <path d="M 290 40 L 430 40" stroke="#27ae60" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="360" y="35" text-anchor="middle" font-size="8" fill="#27ae60">ICMP Echo Request</text>
                    
                    <path d="M 430 60 L 290 60" stroke="#f39c12" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="360" y="75" text-anchor="middle" font-size="8" fill="#f39c12">ICMP Echo Reply</text>
                </g>
                
                <!-- traceroute -->
                <g transform="translate(50, 200)">
                    <rect x="0" y="0" width="180" height="100" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">traceroute</text>
                    <text x="90" y="50" text-anchor="middle" fill="white" font-size="12">経路追跡</text>
                    <text x="90" y="70" text-anchor="middle" fill="white" font-size="10">どこを通ってアクセスするか</text>
                    
                    <!-- traceroute の流れ -->
                    <circle cx="250" cy="50" r="15" fill="#ecf0f1"/>
                    <text x="250" y="55" text-anchor="middle" font-size="10">PC</text>
                    
                    <circle cx="350" cy="50" r="15" fill="#f39c12"/>
                    <text x="350" y="55" text-anchor="middle" font-size="8">Router1</text>
                    
                    <circle cx="450" cy="50" r="15" fill="#f39c12"/>
                    <text x="450" y="55" text-anchor="middle" font-size="8">Router2</text>
                    
                    <circle cx="550" cy="50" r="15" fill="#27ae60"/>
                    <text x="550" y="55" text-anchor="middle" font-size="8">Server</text>
                    
                    <!-- 経路線 -->
                    <path d="M 265 50 L 335 50" stroke="#3498db" stroke-width="2"/>
                    <path d="M 365 50 L 435 50" stroke="#3498db" stroke-width="2"/>
                    <path d="M 465 50 L 535 50" stroke="#3498db" stroke-width="2"/>
                    
                    <text x="400" y="80" text-anchor="middle" font-size="8" fill="#7f8c8d">1. 192.168.1.1  →  2. 203.0.113.1  →  3. 198.51.100.1</text>
                </g>
                
                <!-- netstat -->
                <g transform="translate(50, 340)">
                    <rect x="0" y="0" width="180" height="100" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">netstat</text>
                    <text x="90" y="50" text-anchor="middle" fill="white" font-size="12">接続状況表示</text>
                    <text x="90" y="70" text-anchor="middle" fill="white" font-size="10">開いているポートを確認</text>
                    
                    <!-- netstat 出力例 -->
                    <rect x="250" y="10" width="400" height="80" fill="#2c3e50"/>
                    <text x="260" y="30" fill="#27ae60" font-family="monospace" font-size="8">Proto Local Address    Foreign Address  State</text>
                    <text x="260" y="45" fill="#95a5a6" font-family="monospace" font-size="8">tcp   0.0.0.0:22       *:*              LISTEN</text>
                    <text x="260" y="60" fill="#95a5a6" font-family="monospace" font-size="8">tcp   0.0.0.0:80       *:*              LISTEN</text>
                    <text x="260" y="75" fill="#95a5a6" font-family="monospace" font-size="8">tcp   192.168.1.10:22  192.168.1.5:1234 ESTABLISHED</text>
                </g>
                
                <!-- nslookup/dig -->
                <g transform="translate(450, 60)">
                    <rect x="0" y="0" width="180" height="100" fill="#9b59b6" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="25" text-anchor="middle" fill="white" font-size="16" font-weight="bold">nslookup</text>
                    <text x="90" y="45" text-anchor="middle" fill="white" font-size="16" font-weight="bold">dig</text>
                    <text x="90" y="65" text-anchor="middle" fill="white" font-size="12">DNS問い合わせ</text>
                    <text x="90" y="80" text-anchor="middle" fill="white" font-size="10">ドメイン名↔IPアドレス変換</text>
                </g>
                
                <!-- wget/curl -->
                <g transform="translate(450, 200)">
                    <rect x="0" y="0" width="180" height="100" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="25" text-anchor="middle" fill="white" font-size="16" font-weight="bold">wget</text>
                    <text x="90" y="45" text-anchor="middle" fill="white" font-size="16" font-weight="bold">curl</text>
                    <text x="90" y="65" text-anchor="middle" fill="white" font-size="12">HTTP通信</text>
                    <text x="90" y="80" text-anchor="middle" fill="white" font-size="10">ファイルダウンロード・API</text>
                </g>
                
                <!-- nc -->
                <g transform="translate(450, 340)">
                    <rect x="0" y="0" width="180" height="100" fill="#1abc9c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">nc (netcat)</text>
                    <text x="90" y="50" text-anchor="middle" fill="white" font-size="12">汎用通信</text>
                    <text x="90" y="70" text-anchor="middle" fill="white" font-size="10">ポート接続・データ送信</text>
                </g>
                
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#27ae60"/>
                    </marker>
                </defs>
            </svg>
        </div>
        
        <div class="command-grid">
            <div class="command-card">
                <h3>ping - 疎通確認</h3>
                <div class="command-box">$ ping google.com</div>
                <div class="output-box">
PING google.com (172.217.161.78): 56 data bytes<br>
64 bytes from 172.217.161.78: icmp_seq=0 time=10.123 ms
                </div>
                <p>応答時間とパケットロスを確認</p>
            </div>
            
            <div class="command-card">
                <h3>curl - HTTP通信</h3>
                <div class="command-box">$ curl -I https://example.com</div>
                <div class="command-box">$ curl -o file.html https://example.com</div>
                <p><code>-I</code>: ヘッダーのみ　<code>-o</code>: ファイル保存</p>
            </div>
            
            <div class="command-card">
                <h3>netstat - 接続状況</h3>
                <div class="command-box">$ netstat -tuln</div>
                <div class="command-box">$ netstat -r</div>
                <p><code>-t</code>: TCP　<code>-u</code>: UDP　<code>-l</code>: 待機中<br><code>-n</code>: 数値表示　<code>-r</code>: ルーティングテーブル</p>
            </div>
            
            <div class="command-card">
                <h3>nslookup - DNS問い合わせ</h3>
                <div class="command-box">$ nslookup google.com</div>
                <div class="command-box">$ dig +short google.com</div>
                <p>ドメイン名からIPアドレスを取得</p>
            </div>
        </div>
        
        <div class="key-point">
            <strong>トラブルシューティングの手順：</strong>
            <ol style="margin: 5px 0;">
                <li><code>ping</code>で基本的な疎通確認</li>
                <li><code>traceroute</code>で経路を確認</li>
                <li><code>nslookup</code>でDNS解決を確認</li>
                <li><code>netstat</code>で待機ポートを確認</li>
                <li><code>curl/nc</code>で個別サービスをテスト</li>
            </ol>
        </div>
</div>