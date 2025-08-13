---
layout: chapter
title: "第2章：基本操作マスター"
chapter: 2
---
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第2章：基本操作マスター</title>
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
            border-bottom: 3px solid #e74c3c;
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
        .output-box {
            background: #34495e;
            color: #95a5a6;
            padding: 10px 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            margin: 10px 0;
        }
        .explanation {
            background: #ecf0f1;
            padding: 15px;
            border-left: 4px solid #e74c3c;
            margin: 20px 0;
        }
        .key-point {
            background: #ffe5e5;
            padding: 10px 15px;
            border-radius: 4px;
            margin: 15px 0;
        }
        svg {
            max-width: 100%;
            height: auto;
        }
        .command-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .command-card {
            background: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            padding: 15px;
        }
        .command-card h3 {
            margin: 0 0 10px 0;
            color: #495057;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <div class="section">
        <h1>第2章：基本操作マスター</h1>
        
        <h2>2.1 必須コマンド10選</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">必須コマンドマップ</text>
                
                <!-- カテゴリ1: ナビゲーション -->
                <g transform="translate(50, 60)">
                    <rect x="0" y="0" width="200" height="150" fill="#3498db" opacity="0.2" rx="10"/>
                    <text x="100" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">ナビゲーション</text>
                    
                    <rect x="10" y="40" width="80" height="30" fill="#3498db" rx="5"/>
                    <text x="50" y="58" text-anchor="middle" fill="white" font-size="14">pwd</text>
                    <text x="50" y="85" text-anchor="middle" font-size="10">現在地表示</text>
                    
                    <rect x="110" y="40" width="80" height="30" fill="#3498db" rx="5"/>
                    <text x="150" y="58" text-anchor="middle" fill="white" font-size="14">cd</text>
                    <text x="150" y="85" text-anchor="middle" font-size="10">移動</text>
                    
                    <rect x="60" y="100" width="80" height="30" fill="#3498db" rx="5"/>
                    <text x="100" y="118" text-anchor="middle" fill="white" font-size="14">ls</text>
                    <text x="100" y="145" text-anchor="middle" font-size="10">一覧表示</text>
                </g>
                
                <!-- カテゴリ2: ファイル操作 -->
                <g transform="translate(300, 60)">
                    <rect x="0" y="0" width="250" height="150" fill="#e74c3c" opacity="0.2" rx="10"/>
                    <text x="125" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">ファイル操作</text>
                    
                    <rect x="10" y="40" width="70" height="30" fill="#e74c3c" rx="5"/>
                    <text x="45" y="58" text-anchor="middle" fill="white" font-size="14">cp</text>
                    <text x="45" y="85" text-anchor="middle" font-size="10">コピー</text>
                    
                    <rect x="90" y="40" width="70" height="30" fill="#e74c3c" rx="5"/>
                    <text x="125" y="58" text-anchor="middle" fill="white" font-size="14">mv</text>
                    <text x="125" y="85" text-anchor="middle" font-size="10">移動/改名</text>
                    
                    <rect x="170" y="40" width="70" height="30" fill="#e74c3c" rx="5"/>
                    <text x="205" y="58" text-anchor="middle" fill="white" font-size="14">rm</text>
                    <text x="205" y="85" text-anchor="middle" font-size="10">削除</text>
                    
                    <rect x="50" y="100" width="70" height="30" fill="#e74c3c" rx="5"/>
                    <text x="85" y="118" text-anchor="middle" fill="white" font-size="14">mkdir</text>
                    <text x="85" y="145" text-anchor="middle" font-size="10">フォルダ作成</text>
                    
                    <rect x="130" y="100" width="70" height="30" fill="#e74c3c" rx="5"/>
                    <text x="165" y="118" text-anchor="middle" fill="white" font-size="14">touch</text>
                    <text x="165" y="145" text-anchor="middle" font-size="10">ファイル作成</text>
                </g>
                
                <!-- カテゴリ3: 内容確認 -->
                <g transform="translate(600, 60)">
                    <rect x="0" y="0" width="200" height="150" fill="#27ae60" opacity="0.2" rx="10"/>
                    <text x="100" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">内容確認</text>
                    
                    <rect x="10" y="40" width="80" height="30" fill="#27ae60" rx="5"/>
                    <text x="50" y="58" text-anchor="middle" fill="white" font-size="14">cat</text>
                    <text x="50" y="85" text-anchor="middle" font-size="10">全文表示</text>
                    
                    <rect x="110" y="40" width="80" height="30" fill="#27ae60" rx="5"/>
                    <text x="150" y="58" text-anchor="middle" fill="white" font-size="14">grep</text>
                    <text x="150" y="85" text-anchor="middle" font-size="10">検索</text>
                </g>
                
                <!-- 実行例エリア -->
                <g transform="translate(50, 250)">
                    <rect x="0" y="0" width="750" height="300" fill="#2c3e50" rx="10"/>
                    <text x="20" y="30" fill="#27ae60" font-family="monospace" font-size="14">$ pwd</text>
                    <text x="20" y="50" fill="#95a5a6" font-family="monospace" font-size="12">/home/user</text>
                    
                    <text x="20" y="80" fill="#27ae60" font-family="monospace" font-size="14">$ ls -la</text>
                    <text x="20" y="100" fill="#95a5a6" font-family="monospace" font-size="12">total 24</text>
                    <text x="20" y="120" fill="#95a5a6" font-family="monospace" font-size="12">drwxr-xr-x  3 user user 4096 Jan 15 10:30 .</text>
                    <text x="20" y="140" fill="#95a5a6" font-family="monospace" font-size="12">drwxr-xr-x 10 root root 4096 Jan 10 09:15 ..</text>
                    <text x="20" y="160" fill="#95a5a6" font-family="monospace" font-size="12">-rw-r--r--  1 user user  220 Jan 10 09:15 .bashrc</text>
                    <text x="20" y="180" fill="#95a5a6" font-family="monospace" font-size="12">drwxr-xr-x  2 user user 4096 Jan 15 10:30 Documents</text>
                    
                    <text x="20" y="210" fill="#27ae60" font-family="monospace" font-size="14">$ cd Documents</text>
                    <text x="20" y="230" fill="#27ae60" font-family="monospace" font-size="14">$ touch report.txt</text>
                    <text x="20" y="250" fill="#27ae60" font-family="monospace" font-size="14">$ echo "Hello Linux" > report.txt</text>
                    <text x="20" y="270" fill="#27ae60" font-family="monospace" font-size="14">$ cat report.txt</text>
                    <text x="20" y="290" fill="#95a5a6" font-family="monospace" font-size="12">Hello Linux</text>
                </g>
            </svg>
        </div>
        
        <div class="command-grid">
            <div class="command-card">
                <h3>pwd</h3>
                <div class="command-box">$ pwd</div>
                <p>現在のディレクトリパスを表示</p>
            </div>
            
            <div class="command-card">
                <h3>ls</h3>
                <div class="command-box">$ ls -la</div>
                <p>ファイル・フォルダ一覧を詳細表示</p>
            </div>
            
            <div class="command-card">
                <h3>cd</h3>
                <div class="command-box">$ cd /path/to/dir</div>
                <p>指定ディレクトリへ移動</p>
            </div>
            
            <div class="command-card">
                <h3>cp</h3>
                <div class="command-box">$ cp file1 file2</div>
                <p>file1をfile2にコピー</p>
            </div>
            
            <div class="command-card">
                <h3>mv</h3>
                <div class="command-box">$ mv old new</div>
                <p>ファイル移動または名前変更</p>
            </div>
            
            <div class="command-card">
                <h3>rm</h3>
                <div class="command-box">$ rm -rf dir</div>
                <p>ファイル・ディレクトリ削除</p>
            </div>
        </div>
        
        <h2>2.2 パーミッションの考え方</h2>
        
        <div class="diagram-container">
            <svg width="850" height="500" viewBox="0 0 850 500">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ファイルの権限 = 鍵と扉</text>
                
                <!-- パーミッション表示 -->
                <g transform="translate(50, 60)">
                    <rect x="0" y="0" width="750" height="100" fill="#34495e" rx="10"/>
                    <text x="20" y="35" fill="white" font-family="monospace" font-size="16">-rwxr-xr--  1 user group 1024 Jan 15 10:30 script.sh</text>
                    
                    <!-- 区切り線 -->
                    <line x1="30" y1="50" x2="30" y2="90" stroke="#e74c3c" stroke-width="2"/>
                    <line x1="105" y1="50" x2="105" y2="90" stroke="#3498db" stroke-width="2"/>
                    <line x1="180" y1="50" x2="180" y2="90" stroke="#27ae60" stroke-width="2"/>
                    <line x1="255" y1="50" x2="255" y2="90" stroke="#f39c12" stroke-width="2"/>
                    
                    <!-- ラベル -->
                    <text x="30" y="85" text-anchor="middle" fill="#e74c3c" font-size="10">種類</text>
                    <text x="67" y="85" text-anchor="middle" fill="#3498db" font-size="10">所有者</text>
                    <text x="142" y="85" text-anchor="middle" fill="#27ae60" font-size="10">グループ</text>
                    <text x="217" y="85" text-anchor="middle" fill="#f39c12" font-size="10">その他</text>
                </g>
                
                <!-- 権限の説明 -->
                <g transform="translate(100, 200)">
                    <text x="0" y="0" font-size="16" font-weight="bold" fill="#2c3e50">権限の記号</text>
                    
                    <!-- r -->
                    <rect x="0" y="20" width="60" height="60" fill="#3498db" rx="5"/>
                    <text x="30" y="55" text-anchor="middle" fill="white" font-size="24" font-weight="bold">r</text>
                    <text x="30" y="100" text-anchor="middle" font-size="12">読み取り</text>
                    <text x="30" y="115" text-anchor="middle" font-size="10">(Read)</text>
                    
                    <!-- w -->
                    <rect x="100" y="20" width="60" height="60" fill="#e74c3c" rx="5"/>
                    <text x="130" y="55" text-anchor="middle" fill="white" font-size="24" font-weight="bold">w</text>
                    <text x="130" y="100" text-anchor="middle" font-size="12">書き込み</text>
                    <text x="130" y="115" text-anchor="middle" font-size="10">(Write)</text>
                    
                    <!-- x -->
                    <rect x="200" y="20" width="60" height="60" fill="#27ae60" rx="5"/>
                    <text x="230" y="55" text-anchor="middle" fill="white" font-size="24" font-weight="bold">x</text>
                    <text x="230" y="100" text-anchor="middle" font-size="12">実行</text>
                    <text x="230" y="115" text-anchor="middle" font-size="10">(eXecute)</text>
                </g>
                
                <!-- 鍵のアナロジー -->
                <g transform="translate(450, 200)">
                    <text x="150" y="0" font-size="16" font-weight="bold" fill="#2c3e50">鍵に例えると...</text>
                    
                    <!-- 部屋 -->
                    <rect x="50" y="20" width="250" height="180" fill="none" stroke="#34495e" stroke-width="3" rx="10"/>
                    <text x="175" y="45" text-anchor="middle" font-size="14" font-weight="bold">ファイル = 部屋</text>
                    
                    <!-- 3つの鍵 -->
                    <g transform="translate(80, 70)">
                        <!-- 鍵1: r -->
                        <circle cx="0" cy="0" r="20" fill="#3498db"/>
                        <text x="0" y="5" text-anchor="middle" fill="white" font-size="14" font-weight="bold">r</text>
                        <rect x="-10" y="20" width="20" height="25" fill="#3498db"/>
                        <text x="0" y="60" text-anchor="middle" font-size="10">覗き見OK</text>
                    </g>
                    
                    <g transform="translate(175, 70)">
                        <!-- 鍵2: w -->
                        <circle cx="0" cy="0" r="20" fill="#e74c3c"/>
                        <text x="0" y="5" text-anchor="middle" fill="white" font-size="14" font-weight="bold">w</text>
                        <rect x="-10" y="20" width="20" height="25" fill="#e74c3c"/>
                        <text x="0" y="60" text-anchor="middle" font-size="10">模様替えOK</text>
                    </g>
                    
                    <g transform="translate(270, 70)">
                        <!-- 鍵3: x -->
                        <circle cx="0" cy="0" r="20" fill="#27ae60"/>
                        <text x="0" y="5" text-anchor="middle" fill="white" font-size="14" font-weight="bold">x</text>
                        <rect x="-10" y="20" width="20" height="25" fill="#27ae60"/>
                        <text x="0" y="60" text-anchor="middle" font-size="10">入室OK</text>
                    </g>
                    
                    <!-- 人のグループ -->
                    <text x="70" y="160" font-size="12">所有者</text>
                    <text x="145" y="160" font-size="12">グループ</text>
                    <text x="230" y="160" font-size="12">その他</text>
                </g>
                
                <!-- chmod例 -->
                <g transform="translate(50, 350)">
                    <rect x="0" y="0" width="750" height="120" fill="#2c3e50" rx="10"/>
                    <text x="20" y="30" fill="#27ae60" font-family="monospace" font-size="14">$ ls -l script.sh</text>
                    <text x="20" y="50" fill="#95a5a6" font-family="monospace" font-size="12">-rw-r--r--  1 user group 1024 Jan 15 10:30 script.sh</text>
                    <text x="20" y="75" fill="#27ae60" font-family="monospace" font-size="14">$ chmod +x script.sh    # 実行権限を追加</text>
                    <text x="20" y="95" fill="#27ae60" font-family="monospace" font-size="14">$ ls -l script.sh</text>
                    <text x="20" y="115" fill="#95a5a6" font-family="monospace" font-size="12">-rwxr-xr-x  1 user group 1024 Jan 15 10:30 script.sh</text>
                </g>
            </svg>
        </div>
        
        <div class="key-point">
            <strong>chmod数値表記：</strong>
            r=4, w=2, x=1 を足し算
            <ul style="margin: 5px 0;">
                <li>755 = rwxr-xr-x (所有者:全権限、他:読み実行)</li>
                <li>644 = rw-r--r-- (所有者:読み書き、他:読みのみ)</li>
                <li>600 = rw------- (所有者のみアクセス可)</li>
            </ul>
        </div>
        
        <h2>2.3 プロセスとは</h2>
        
        <div class="diagram-container">
            <svg width="850" height="550" viewBox="0 0 850 550">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">プロセス = 実行中のプログラム</text>
                
                <!-- 工場のアナロジー -->
                <g transform="translate(50, 60)">
                    <text x="200" y="0" font-size="16" font-weight="bold" fill="#2c3e50">工場のライン作業に例えると...</text>
                    
                    <!-- 工場建物 -->
                    <rect x="0" y="20" width="400" height="200" fill="none" stroke="#34495e" stroke-width="3" rx="10"/>
                    <text x="200" y="45" text-anchor="middle" font-size="14" font-weight="bold">システム = 工場</text>
                    
                    <!-- ライン1 -->
                    <rect x="20" y="70" width="360" height="40" fill="#3498db" opacity="0.3" rx="5"/>
                    <circle cx="50" cy="90" r="15" fill="#3498db"/>
                    <text x="50" y="95" text-anchor="middle" fill="white" font-size="10">PID</text>
                    <text x="50" y="105" text-anchor="middle" fill="white" font-size="10">1234</text>
                    <rect x="80" y="80" width="60" height="20" fill="#3498db"/>
                    <text x="110" y="95" text-anchor="middle" fill="white" font-size="10">nginx</text>
                    <text x="220" y="95" text-anchor="middle" font-size="12">→ Webサーバー稼働中</text>
                    
                    <!-- ライン2 -->
                    <rect x="20" y="120" width="360" height="40" fill="#e74c3c" opacity="0.3" rx="5"/>
                    <circle cx="50" cy="140" r="15" fill="#e74c3c"/>
                    <text x="50" y="145" text-anchor="middle" fill="white" font-size="10">PID</text>
                    <text x="50" y="155" text-anchor="middle" fill="white" font-size="10">5678</text>
                    <rect x="80" y="130" width="60" height="20" fill="#e74c3c"/>
                    <text x="110" y="145" text-anchor="middle" fill="white" font-size="10">mysql</text>
                    <text x="220" y="145" text-anchor="middle" font-size="12">→ データベース稼働中</text>
                    
                    <!-- ライン3 -->
                    <rect x="20" y="170" width="360" height="40" fill="#27ae60" opacity="0.3" rx="5"/>
                    <circle cx="50" cy="190" r="15" fill="#27ae60"/>
                    <text x="50" y="195" text-anchor="middle" fill="white" font-size="10">PID</text>
                    <text x="50" y="205" text-anchor="middle" fill="white" font-size="10">9012</text>
                    <rect x="80" y="180" width="60" height="20" fill="#27ae60"/>
                    <text x="110" y="195" text-anchor="middle" fill="white" font-size="10">sshd</text>
                    <text x="220" y="195" text-anchor="middle" font-size="12">→ リモート接続待機中</text>
                </g>
                
                <!-- プロセスの状態 -->
                <g transform="translate(500, 80)">
                    <text x="125" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">プロセスの状態</text>
                    
                    <!-- Running -->
                    <circle cx="125" cy="50" r="30" fill="#27ae60"/>
                    <text x="125" y="55" text-anchor="middle" fill="white" font-size="12">実行中</text>
                    <text x="125" y="95" text-anchor="middle" font-size="10">(Running)</text>
                    
                    <!-- Sleeping -->
                    <circle cx="125" cy="140" r="30" fill="#f39c12"/>
                    <text x="125" y="145" text-anchor="middle" fill="white" font-size="12">待機中</text>
                    <text x="125" y="185" text-anchor="middle" font-size="10">(Sleeping)</text>
                    
                    <!-- Stopped -->
                    <circle cx="250" cy="90" r="30" fill="#e74c3c"/>
                    <text x="250" y="95" text-anchor="middle" fill="white" font-size="12">停止</text>
                    <text x="250" y="135" text-anchor="middle" font-size="10">(Stopped)</text>
                    
                    <!-- Zombie -->
                    <circle cx="250" cy="180" r="30" fill="#95a5a6"/>
                    <text x="250" y="185" text-anchor="middle" fill="white" font-size="12">ゾンビ</text>
                    <text x="250" y="225" text-anchor="middle" font-size="10">(Zombie)</text>
                    
                    <!-- 矢印 -->
                    <path d="M 155 50 L 220 90" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <path d="M 125 80 L 125 110" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <path d="M 155 140 L 220 180" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                </g>
                
                <!-- プロセス管理コマンド -->
                <g transform="translate(50, 300)">
                    <rect x="0" y="0" width="750" height="220" fill="#2c3e50" rx="10"/>
                    <text x="20" y="30" fill="#27ae60" font-family="monospace" font-size="14">$ ps aux | head -5</text>
                    <text x="20" y="50" fill="#95a5a6" font-family="monospace" font-size="11">USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND</text>
                    <text x="20" y="70" fill="#95a5a6" font-family="monospace" font-size="11">root         1  0.0  0.1 225768  9572 ?        Ss   Jan10   0:05 /sbin/init</text>
                    <text x="20" y="90" fill="#95a5a6" font-family="monospace" font-size="11">root        89  0.0  0.0      0     0 ?        S    Jan10   0:00 [kworker]</text>
                    <text x="20" y="110" fill="#95a5a6" font-family="monospace" font-size="11">www-data  1234  0.2  0.5 325768 45572 ?        S    10:30   0:15 nginx</text>
                    <text x="20" y="130" fill="#95a5a6" font-family="monospace" font-size="11">mysql     5678  1.5  2.1 825768 85572 ?        Sl   10:31   1:25 mysqld</text>
                    
                    <text x="20" y="160" fill="#27ae60" font-family="monospace" font-size="14">$ kill 1234        # プロセスに終了シグナル送信</text>
                    <text x="20" y="180" fill="#27ae60" font-family="monospace" font-size="14">$ kill -9 1234     # 強制終了</text>
                    <text x="20" y="200" fill="#27ae60" font-family="monospace" font-size="14">$ top              # リアルタイムでプロセス監視</text>
                </g>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>重要コマンド：</strong>
            <ul>
                <li><code>ps aux</code> - 全プロセス表示</li>
                <li><code>top</code> / <code>htop</code> - リアルタイム監視</li>
                <li><code>kill PID</code> - プロセス終了</li>
                <li><code>kill -9 PID</code> - 強制終了</li>
                <li><code>jobs</code> - バックグラウンドジョブ表示</li>
                <li><code>&</code> - コマンドをバックグラウンド実行</li>
            </ul>
        </div>
        
        <div class="key-point">
            <strong>PID（Process ID）：</strong>各プロセスに割り当てられる一意の識別番号。プロセス管理の際はこの番号を使用。
        </div>
    </div>
</body>
</html>