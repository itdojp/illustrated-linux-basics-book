---
layout: chapter
title: "第1章：Linuxの世界地図"
chapter: 1
---

<div class="section">
        <h1>第1章：Linuxの世界地図</h1>
        
        <h2>1.1 Linuxディストリビューション全体像</h2>
        
        <div class="diagram-container">
            <svg width="900" height="600" viewBox="0 0 900 600">
                <!-- Linux Kernel (中心) -->
                <circle cx="450" cy="300" r="80" fill="#2c3e50"/>
                <text x="450" y="305" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Linux カーネル</text>
                <text x="450" y="325" text-anchor="middle" fill="white" font-size="12">（核心部分）</text>
                
                <!-- Debian系 -->
                <g transform="translate(150, 100)">
                    <rect x="0" y="0" width="120" height="60" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="60" y="35" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Debian</text>
                    
                    <!-- Ubuntu -->
                    <rect x="-30" y="-80" width="80" height="40" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="10" y="-55" text-anchor="middle" fill="white" font-size="14">Ubuntu</text>
                    
                    <!-- Linux Mint -->
                    <rect x="70" y="-80" width="80" height="40" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="110" y="-55" text-anchor="middle" fill="white" font-size="14">Linux Mint</text>
                    
                    <line x1="10" y1="-40" x2="30" y2="0" stroke="#7f8c8d" stroke-width="2"/>
                    <line x1="110" y1="-40" x2="90" y2="0" stroke="#7f8c8d" stroke-width="2"/>
                </g>
                
                <!-- Red Hat系 -->
                <g transform="translate(630, 100)">
                    <rect x="0" y="0" width="120" height="60" fill="#c0392b" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="60" y="35" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Red Hat</text>
                    
                    <!-- CentOS/Rocky -->
                    <rect x="-30" y="-80" width="80" height="40" fill="#8e44ad" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="10" y="-55" text-anchor="middle" fill="white" font-size="14">Rocky</text>
                    
                    <!-- Fedora -->
                    <rect x="70" y="-80" width="80" height="40" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="110" y="-55" text-anchor="middle" fill="white" font-size="14">Fedora</text>
                    
                    <line x1="10" y1="-40" x2="30" y2="0" stroke="#7f8c8d" stroke-width="2"/>
                    <line x1="110" y1="-40" x2="90" y2="0" stroke="#7f8c8d" stroke-width="2"/>
                </g>
                
                <!-- Arch系 -->
                <g transform="translate(150, 400)">
                    <rect x="0" y="0" width="120" height="60" fill="#1abc9c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="60" y="35" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Arch Linux</text>
                    
                    <!-- Manjaro -->
                    <rect x="20" y="80" width="80" height="40" fill="#16a085" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="60" y="105" text-anchor="middle" fill="white" font-size="14">Manjaro</text>
                    
                    <line x1="60" y1="60" x2="60" y2="80" stroke="#7f8c8d" stroke-width="2"/>
                </g>
                
                <!-- SUSE系 -->
                <g transform="translate(630, 400)">
                    <rect x="0" y="0" width="120" height="60" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="60" y="35" text-anchor="middle" fill="white" font-size="16" font-weight="bold">SUSE</text>
                    
                    <!-- openSUSE -->
                    <rect x="20" y="80" width="80" height="40" fill="#229954" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="60" y="105" text-anchor="middle" fill="white" font-size="14">openSUSE</text>
                    
                    <line x1="60" y1="60" x2="60" y2="80" stroke="#7f8c8d" stroke-width="2"/>
                </g>
                
                <!-- その他独立系 -->
                <g transform="translate(390, 480)">
                    <rect x="0" y="0" width="120" height="40" fill="#95a5a6" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="60" y="25" text-anchor="middle" fill="white" font-size="14">Gentoo</text>
                </g>
                
                <!-- カーネルから各系統への線 -->
                <line x1="380" y1="280" x2="270" y2="160" stroke="#7f8c8d" stroke-width="2" stroke-dasharray="5,5"/>
                <line x1="520" y1="280" x2="630" y2="160" stroke="#7f8c8d" stroke-width="2" stroke-dasharray="5,5"/>
                <line x1="380" y1="320" x2="270" y2="430" stroke="#7f8c8d" stroke-width="2" stroke-dasharray="5,5"/>
                <line x1="520" y1="320" x2="630" y2="430" stroke="#7f8c8d" stroke-width="2" stroke-dasharray="5,5"/>
                <line x1="450" y1="380" x2="450" y2="480" stroke="#7f8c8d" stroke-width="2" stroke-dasharray="5,5"/>
                
                <!-- 凡例 -->
                <g transform="translate(50, 50)">
                    <text x="0" y="0" font-size="14" font-weight="bold" fill="#2c3e50">特徴：</text>
                    <text x="0" y="25" font-size="12" fill="#e74c3c">■ Debian系: 安定性重視</text>
                    <text x="0" y="45" font-size="12" fill="#c0392b">■ Red Hat系: 企業向け</text>
                    <text x="0" y="65" font-size="12" fill="#1abc9c">■ Arch系: 最新技術</text>
                    <text x="0" y="85" font-size="12" fill="#27ae60">■ SUSE系: 欧州で人気</text>
                </g>
            </svg>
        </div>
        
        <div class="key-point">
            <strong>選択の指針：</strong>
            <ul style="margin: 5px 0;">
                <li>初心者・デスクトップ → Ubuntu</li>
                <li>企業サーバー → Red Hat Enterprise Linux / Rocky Linux</li>
                <li>最新技術を試したい → Arch Linux / Fedora</li>
            </ul>
        </div>
        
        <h2>1.2 コマンドとGUIの違い</h2>
        
        <div class="diagram-container">
            <svg width="850" height="500" viewBox="0 0 850 500">
                <!-- GUI側 -->
                <g transform="translate(50, 50)">
                    <text x="175" y="0" text-anchor="middle" font-size="20" font-weight="bold" fill="#3498db">GUI（グラフィカル）</text>
                    
                    <!-- ウィンドウ -->
                    <rect x="50" y="30" width="250" height="180" fill="#ecf0f1" stroke="#34495e" stroke-width="2"/>
                    <rect x="50" y="30" width="250" height="25" fill="#3498db"/>
                    <circle cx="70" cy="42" r="5" fill="#e74c3c"/>
                    <circle cx="85" cy="42" r="5" fill="#f39c12"/>
                    <circle cx="100" cy="42" r="5" fill="#27ae60"/>
                    <text x="175" y="47" text-anchor="middle" fill="white" font-size="12">ファイルマネージャー</text>
                    
                    <!-- フォルダアイコン -->
                    <rect x="70" y="80" width="40" height="35" fill="#f39c12"/>
                    <rect x="130" y="80" width="40" height="35" fill="#f39c12"/>
                    <rect x="190" y="80" width="40" height="35" fill="#f39c12"/>
                    <text x="90" y="135" text-anchor="middle" font-size="10">Documents</text>
                    <text x="150" y="135" text-anchor="middle" font-size="10">Pictures</text>
                    <text x="210" y="135" text-anchor="middle" font-size="10">Downloads</text>
                    
                    <!-- マウスポインタ -->
                    <path d="M 150 160 L 140 180 L 155 175 Z" fill="#2c3e50"/>
                    <text x="165" y="178" font-size="10">クリック</text>
                </g>
                
                <!-- CLI側 -->
                <g transform="translate(450, 50)">
                    <text x="175" y="0" text-anchor="middle" font-size="20" font-weight="bold" fill="#27ae60">CLI（コマンドライン）</text>
                    
                    <!-- ターミナル -->
                    <rect x="50" y="30" width="300" height="180" fill="#2c3e50" stroke="#34495e" stroke-width="2"/>
                    <text x="60" y="55" fill="#27ae60" font-family="monospace" font-size="12">$ ls -la</text>
                    <text x="60" y="75" fill="#95a5a6" font-family="monospace" font-size="11">drwxr-xr-x  5 user user 4096 Jan 15 10:30 .</text>
                    <text x="60" y="95" fill="#95a5a6" font-family="monospace" font-size="11">drwxr-xr-x  3 user user 4096 Jan 10 09:15 ..</text>
                    <text x="60" y="115" fill="#95a5a6" font-family="monospace" font-size="11">drwxr-xr-x  2 user user 4096 Jan 12 14:22 Documents</text>
                    <text x="60" y="135" fill="#95a5a6" font-family="monospace" font-size="11">drwxr-xr-x  2 user user 4096 Jan 14 16:45 Pictures</text>
                    <text x="60" y="155" fill="#95a5a6" font-family="monospace" font-size="11">drwxr-xr-x  2 user user 4096 Jan 15 10:30 Downloads</text>
                    <text x="60" y="180" fill="#27ae60" font-family="monospace" font-size="12">$ cd Documents</text>
                    <text x="60" y="200" fill="#27ae60" font-family="monospace" font-size="12">$ █</text>
                </g>
                
                <!-- 比較表 -->
                <g transform="translate(50, 250)">
                    <text x="375" y="20" text-anchor="middle" font-size="18" font-weight="bold" fill="#2c3e50">同じ操作の比較</text>
                    
                    <!-- ヘッダー -->
                    <rect x="100" y="40" width="150" height="30" fill="#34495e"/>
                    <text x="175" y="60" text-anchor="middle" fill="white" font-size="14">操作内容</text>
                    
                    <rect x="250" y="40" width="200" height="30" fill="#3498db"/>
                    <text x="350" y="60" text-anchor="middle" fill="white" font-size="14">GUI</text>
                    
                    <rect x="450" y="40" width="200" height="30" fill="#27ae60"/>
                    <text x="550" y="60" text-anchor="middle" fill="white" font-size="14">CLI</text>
                    
                    <!-- 行1 -->
                    <rect x="100" y="70" width="150" height="40" fill="#ecf0f1" stroke="#95a5a6"/>
                    <text x="175" y="95" text-anchor="middle" font-size="12">ファイル一覧</text>
                    
                    <rect x="250" y="70" width="200" height="40" fill="white" stroke="#95a5a6"/>
                    <text x="350" y="95" text-anchor="middle" font-size="12">フォルダを開く</text>
                    
                    <rect x="450" y="70" width="200" height="40" fill="white" stroke="#95a5a6"/>
                    <text x="550" y="95" text-anchor="middle" font-family="monospace" font-size="12">ls</text>
                    
                    <!-- 行2 -->
                    <rect x="100" y="110" width="150" height="40" fill="#ecf0f1" stroke="#95a5a6"/>
                    <text x="175" y="135" text-anchor="middle" font-size="12">フォルダ移動</text>
                    
                    <rect x="250" y="110" width="200" height="40" fill="white" stroke="#95a5a6"/>
                    <text x="350" y="135" text-anchor="middle" font-size="12">ダブルクリック</text>
                    
                    <rect x="450" y="110" width="200" height="40" fill="white" stroke="#95a5a6"/>
                    <text x="550" y="135" text-anchor="middle" font-family="monospace" font-size="12">cd フォルダ名</text>
                    
                    <!-- 行3 -->
                    <rect x="100" y="150" width="150" height="40" fill="#ecf0f1" stroke="#95a5a6"/>
                    <text x="175" y="175" text-anchor="middle" font-size="12">ファイル削除</text>
                    
                    <rect x="250" y="150" width="200" height="40" fill="white" stroke="#95a5a6"/>
                    <text x="350" y="175" text-anchor="middle" font-size="12">右クリック→削除</text>
                    
                    <rect x="450" y="150" width="200" height="40" fill="white" stroke="#95a5a6"/>
                    <text x="550" y="175" text-anchor="middle" font-family="monospace" font-size="12">rm ファイル名</text>
                </g>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>CLIの利点：</strong>
            <ul>
                <li>自動化可能（スクリプト化）</li>
                <li>リモート操作が容易</li>
                <li>一括処理が高速</li>
                <li>システムリソース消費が少ない</li>
            </ul>
        </div>
        
        <h2>1.3 ファイルシステムの構造</h2>
        
        <div class="diagram-container">
            <svg width="800" height="550" viewBox="0 0 800 550">
                <!-- ルートディレクトリ -->
                <rect x="375" y="20" width="50" height="40" fill="#2c3e50"/>
                <text x="400" y="45" text-anchor="middle" fill="white" font-size="16" font-weight="bold">/</text>
                <text x="400" y="80" text-anchor="middle" font-size="12" fill="#7f8c8d">ルート（最上位）</text>
                
                <!-- 第1階層 -->
                <!-- /home -->
                <rect x="100" y="120" width="60" height="35" fill="#3498db"/>
                <text x="130" y="142" text-anchor="middle" fill="white" font-size="14">/home</text>
                <text x="130" y="170" text-anchor="middle" font-size="10" fill="#7f8c8d">ユーザーの家</text>
                <line x1="400" y1="60" x2="130" y2="120" stroke="#7f8c8d" stroke-width="2"/>
                
                <!-- /etc -->
                <rect x="200" y="120" width="60" height="35" fill="#e74c3c"/>
                <text x="230" y="142" text-anchor="middle" fill="white" font-size="14">/etc</text>
                <text x="230" y="170" text-anchor="middle" font-size="10" fill="#7f8c8d">設定ファイル</text>
                <line x1="400" y1="60" x2="230" y2="120" stroke="#7f8c8d" stroke-width="2"/>
                
                <!-- /var -->
                <rect x="300" y="120" width="60" height="35" fill="#f39c12"/>
                <text x="330" y="142" text-anchor="middle" fill="white" font-size="14">/var</text>
                <text x="330" y="170" text-anchor="middle" font-size="10" fill="#7f8c8d">変動データ</text>
                <line x1="400" y1="60" x2="330" y2="120" stroke="#7f8c8d" stroke-width="2"/>
                
                <!-- /usr -->
                <rect x="440" y="120" width="60" height="35" fill="#9b59b6"/>
                <text x="470" y="142" text-anchor="middle" fill="white" font-size="14">/usr</text>
                <text x="470" y="170" text-anchor="middle" font-size="10" fill="#7f8c8d">プログラム</text>
                <line x1="400" y1="60" x2="470" y2="120" stroke="#7f8c8d" stroke-width="2"/>
                
                <!-- /bin -->
                <rect x="540" y="120" width="60" height="35" fill="#1abc9c"/>
                <text x="570" y="142" text-anchor="middle" fill="white" font-size="14">/bin</text>
                <text x="570" y="170" text-anchor="middle" font-size="10" fill="#7f8c8d">基本コマンド</text>
                <line x1="400" y1="60" x2="570" y2="120" stroke="#7f8c8d" stroke-width="2"/>
                
                <!-- /tmp -->
                <rect x="640" y="120" width="60" height="35" fill="#95a5a6"/>
                <text x="670" y="142" text-anchor="middle" fill="white" font-size="14">/tmp</text>
                <text x="670" y="170" text-anchor="middle" font-size="10" fill="#7f8c8d">一時ファイル</text>
                <line x1="400" y1="60" x2="670" y2="120" stroke="#7f8c8d" stroke-width="2"/>
                
                <!-- 第2階層の例 -->
                <!-- /home/user -->
                <rect x="80" y="220" width="100" height="30" fill="#2980b9"/>
                <text x="130" y="240" text-anchor="middle" fill="white" font-size="12">/home/user</text>
                <line x1="130" y1="155" x2="130" y2="220" stroke="#7f8c8d" stroke-width="1"/>
                
                <!-- /var/log -->
                <rect x="280" y="220" width="100" height="30" fill="#e67e22"/>
                <text x="330" y="240" text-anchor="middle" fill="white" font-size="12">/var/log</text>
                <text x="330" y="265" text-anchor="middle" font-size="10" fill="#7f8c8d">ログファイル</text>
                <line x1="330" y1="155" x2="330" y2="220" stroke="#7f8c8d" stroke-width="1"/>
                
                <!-- /usr/bin -->
                <rect x="420" y="220" width="100" height="30" fill="#8e44ad"/>
                <text x="470" y="240" text-anchor="middle" fill="white" font-size="12">/usr/bin</text>
                <text x="470" y="265" text-anchor="middle" font-size="10" fill="#7f8c8d">ユーザーコマンド</text>
                <line x1="470" y1="155" x2="470" y2="220" stroke="#7f8c8d" stroke-width="1"/>
                
                <!-- 建物のアナロジー -->
                <g transform="translate(50, 320)">
                    <text x="350" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">建物に例えると...</text>
                    
                    <!-- ビル全体 -->
                    <rect x="250" y="30" width="300" height="180" fill="none" stroke="#34495e" stroke-width="3"/>
                    
                    <!-- 各階 -->
                    <line x1="250" y1="90" x2="550" y2="90" stroke="#34495e" stroke-width="2"/>
                    <line x1="250" y1="150" x2="550" y2="150" stroke="#34495e" stroke-width="2"/>
                    
                    <!-- ラベル -->
                    <text x="400" y="60" text-anchor="middle" font-size="14" font-weight="bold">/ = ビル全体</text>
                    
                    <rect x="260" y="100" width="80" height="40" fill="#3498db" opacity="0.7"/>
                    <text x="300" y="125" text-anchor="middle" fill="white" font-size="12">/home</text>
                    <text x="300" y="140" text-anchor="middle" font-size="10">住居フロア</text>
                    
                    <rect x="360" y="100" width="80" height="40" fill="#e74c3c" opacity="0.7"/>
                    <text x="400" y="125" text-anchor="middle" fill="white" font-size="12">/etc</text>
                    <text x="400" y="140" text-anchor="middle" font-size="10">管理室</text>
                    
                    <rect x="460" y="100" width="80" height="40" fill="#f39c12" opacity="0.7"/>
                    <text x="500" y="125" text-anchor="middle" fill="white" font-size="12">/var</text>
                    <text x="500" y="140" text-anchor="middle" font-size="10">倉庫</text>
                    
                    <rect x="260" y="160" width="80" height="40" fill="#9b59b6" opacity="0.7"/>
                    <text x="300" y="185" text-anchor="middle" fill="white" font-size="12">/usr</text>
                    <text x="300" y="200" text-anchor="middle" font-size="10">オフィス</text>
                    
                    <rect x="360" y="160" width="80" height="40" fill="#1abc9c" opacity="0.7"/>
                    <text x="400" y="185" text-anchor="middle" fill="white" font-size="12">/bin</text>
                    <text x="400" y="200" text-anchor="middle" font-size="10">工具箱</text>
                    
                    <rect x="460" y="160" width="80" height="40" fill="#95a5a6" opacity="0.7"/>
                    <text x="500" y="185" text-anchor="middle" fill="white" font-size="12">/tmp</text>
                    <text x="500" y="200" text-anchor="middle" font-size="10">ゴミ置き場</text>
                </g>
            </svg>
        </div>
        
        <div class="key-point">
            <strong>重要ディレクトリ：</strong>
            <ul style="margin: 5px 0;">
                <li><code>/home</code> - 各ユーザーの個人領域</li>
                <li><code>/etc</code> - システム全体の設定ファイル</li>
                <li><code>/var/log</code> - システムやアプリケーションのログ</li>
                <li><code>/usr/bin</code> - 一般的なコマンド・プログラム</li>
                <li><code>/tmp</code> - 一時ファイル（再起動で消去）</li>
            </ul>
        </div>
</div>