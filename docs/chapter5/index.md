---
layout: chapter
title: "第5章：実践演習とトラブルシューティング"
chapter: 5
---
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第5章：実践演習とトラブルシューティング</title>
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
            border-bottom: 3px solid #f39c12;
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
        .error-box {
            background: #e74c3c;
            color: white;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            margin: 15px 0;
        }
        .solution-box {
            background: #27ae60;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }
        .explanation {
            background: #ecf0f1;
            padding: 15px;
            border-left: 4px solid #f39c12;
            margin: 20px 0;
        }
        .key-point {
            background: #fff4e5;
            padding: 10px 15px;
            border-radius: 4px;
            margin: 15px 0;
        }
        .exercise-box {
            background: #e8f8f5;
            border: 2px solid #1abc9c;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .exercise-box h3 {
            color: #16a085;
            margin-top: 0;
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
    </style>
</head>
<body>
    <div class="section">
        <h1>第5章：実践演習とトラブルシューティング</h1>
        
        <h2>5.1 Webサーバー構築演習</h2>
        
        <div class="diagram-container">
            <svg width="850" height="500" viewBox="0 0 850 500">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">簡単なWebサービス構築フロー</text>
                
                <!-- Step by Step -->
                <g transform="translate(50, 60)">
                    <!-- Step 1 -->
                    <rect x="0" y="0" width="180" height="120" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="90" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">Step 1: 環境準備</text>
                    <text x="90" y="50" text-anchor="middle" fill="white" font-size="11">✓ Linux起動</text>
                    <text x="90" y="70" text-anchor="middle" fill="white" font-size="11">✓ ネットワーク確認</text>
                    <text x="90" y="90" text-anchor="middle" fill="white" font-size="11">✓ 必要パッケージ</text>
                    <text x="90" y="110" text-anchor="middle" fill="white" font-size="11">　インストール</text>
                    
                    <!-- Arrow -->
                    <path d="M 190 60 L 240 60" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    
                    <!-- Step 2 -->
                    <rect x="250" y="0" width="180" height="120" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="340" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">Step 2: Nginx設定</text>
                    <text x="340" y="50" text-anchor="middle" fill="white" font-size="11">✓ Nginx インストール</text>
                    <text x="340" y="70" text-anchor="middle" fill="white" font-size="11">✓ 設定ファイル編集</text>
                    <text x="340" y="90" text-anchor="middle" fill="white" font-size="11">✓ HTMLファイル配置</text>
                    <text x="340" y="110" text-anchor="middle" fill="white" font-size="11">✓ サービス起動</text>
                    
                    <!-- Arrow -->
                    <path d="M 440 60 L 490 60" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    
                    <!-- Step 3 -->
                    <rect x="500" y="0" width="180" height="120" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="590" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">Step 3: 動作確認</text>
                    <text x="590" y="50" text-anchor="middle" fill="white" font-size="11">✓ ローカル接続テスト</text>
                    <text x="590" y="70" text-anchor="middle" fill="white" font-size="11">✓ ログ確認</text>
                    <text x="590" y="90" text-anchor="middle" fill="white" font-size="11">✓ ファイアウォール</text>
                    <text x="590" y="110" text-anchor="middle" fill="white" font-size="11">✓ 外部アクセス確認</text>
                </g>
                
                <!-- 構成図 -->
                <g transform="translate(50, 220)">
                    <text x="375" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">完成時の構成</text>
                    
                    <!-- クライアント -->
                    <rect x="50" y="30" width="120" height="80" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="110" y="60" text-anchor="middle" fill="white" font-size="12">ブラウザ</text>
                    <text x="110" y="80" text-anchor="middle" fill="white" font-size="10">http://localhost</text>
                    
                    <!-- 矢印 -->
                    <path d="M 180 70 L 270 70" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="225" y="60" text-anchor="middle" font-size="10">HTTP Request</text>
                    <path d="M 270 90 L 180 90" stroke="#7f8c8d" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrowhead)"/>
                    <text x="225" y="105" text-anchor="middle" font-size="10">HTML Response</text>
                    
                    <!-- Nginx -->
                    <rect x="280" y="30" width="150" height="80" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="355" y="60" text-anchor="middle" fill="white" font-size="12">Nginx</text>
                    <text x="355" y="80" text-anchor="middle" fill="white" font-size="10">Port 80</text>
                    
                    <!-- 矢印 -->
                    <path d="M 440 70 L 530 70" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                    <text x="485" y="60" text-anchor="middle" font-size="10">読み込み</text>
                    
                    <!-- HTMLファイル -->
                    <rect x="540" y="30" width="150" height="80" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="615" y="60" text-anchor="middle" fill="white" font-size="12">Webコンテンツ</text>
                    <text x="615" y="80" text-anchor="middle" fill="white" font-size="10">/var/www/html/</text>
                    
                    <!-- システム構成 -->
                    <rect x="50" y="150" width="640" height="80" fill="#ecf0f1" stroke="#34495e" stroke-width="2" rx="10"/>
                    <text x="370" y="175" text-anchor="middle" font-size="14" font-weight="bold" fill="#2c3e50">Linux OS</text>
                    <text x="370" y="200" text-anchor="middle" font-size="12" fill="#7f8c8d">ポート管理、プロセス管理、ファイルシステム</text>
                </g>
                
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#7f8c8d"/>
                    </marker>
                </defs>
            </svg>
        </div>
        
        <div class="exercise-box">
            <h3>演習1: Nginxでシンプルなサイトを立ち上げる</h3>
            
            <div class="command-box">
# 1. Nginxのインストール<br>
$ sudo apt update<br>
$ sudo apt install nginx -y<br><br>

# 2. サービスの起動と確認<br>
$ sudo systemctl start nginx<br>
$ sudo systemctl status nginx<br><br>

# 3. HTMLファイルの作成<br>
$ sudo nano /var/www/html/index.html<br><br>

# 4. ブラウザで確認<br>
# http://localhost または http://[サーバーIP]
            </div>
            
            <p><strong>期待される結果：</strong>ブラウザで作成したHTMLページが表示される</p>
        </div>
        
        <h2>5.2 よくあるエラーと対処法</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- タイトル -->
                <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">トラブルシューティングフローチャート</text>
                
                <!-- スタート -->
                <ellipse cx="425" cy="80" rx="60" ry="30" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                <text x="425" y="85" text-anchor="middle" fill="white" font-size="12">問題発生</text>
                
                <!-- 分岐1: サービス起動？ -->
                <path d="M 425 110 L 425 150" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                
                <rect x="325" y="150" width="200" height="60" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="425" y="180" text-anchor="middle" fill="white" font-size="12">サービスは起動してる？</text>
                <text x="425" y="195" text-anchor="middle" fill="white" font-size="10">systemctl status</text>
                
                <!-- No: 起動していない -->
                <path d="M 325 180 L 200 180" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="262" y="175" font-size="10">No</text>
                
                <rect x="50" y="150" width="150" height="60" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="125" y="175" text-anchor="middle" fill="white" font-size="11">サービス起動</text>
                <text x="125" y="195" text-anchor="middle" fill="white" font-size="10">systemctl start</text>
                
                <!-- Yes: 起動している -->
                <path d="M 425 210 L 425 250" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="445" y="230" font-size="10">Yes</text>
                
                <!-- 分岐2: ポート開いてる？ -->
                <rect x="325" y="250" width="200" height="60" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="425" y="280" text-anchor="middle" fill="white" font-size="12">ポートは開いてる？</text>
                <text x="425" y="295" text-anchor="middle" fill="white" font-size="10">netstat -tuln</text>
                
                <!-- No: ポート未開放 -->
                <path d="M 525 280 L 650 280" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="588" y="275" font-size="10">No</text>
                
                <rect x="650" y="250" width="150" height="60" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="725" y="275" text-anchor="middle" fill="white" font-size="11">ファイアウォール</text>
                <text x="725" y="295" text-anchor="middle" fill="white" font-size="10">設定確認</text>
                
                <!-- Yes: ポート開放済み -->
                <path d="M 425 310 L 425 350" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="445" y="330" font-size="10">Yes</text>
                
                <!-- 分岐3: ログにエラー？ -->
                <rect x="325" y="350" width="200" height="60" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="425" y="380" text-anchor="middle" fill="white" font-size="12">ログにエラーある？</text>
                <text x="425" y="395" text-anchor="middle" fill="white" font-size="10">journalctl -xe</text>
                
                <!-- Yes: エラーあり -->
                <path d="M 325 380 L 200 380" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="262" y="375" font-size="10">Yes</text>
                
                <rect x="50" y="350" width="150" height="60" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="125" y="375" text-anchor="middle" fill="white" font-size="11">エラー内容を</text>
                <text x="125" y="395" text-anchor="middle" fill="white" font-size="11">確認して対処</text>
                
                <!-- No: エラーなし -->
                <path d="M 425 410 L 425 450" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="445" y="430" font-size="10">No</text>
                
                <!-- 設定ファイル確認 -->
                <rect x="325" y="450" width="200" height="60" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="10"/>
                <text x="425" y="475" text-anchor="middle" fill="white" font-size="12">設定ファイル確認</text>
                <text x="425" y="495" text-anchor="middle" fill="white" font-size="10">権限・文法チェック</text>
            </svg>
        </div>
        
        <h2>5.3 よくあるエラー集</h2>
        
        <div class="explanation">
            <h3>エラー1: Permission denied</h3>
            <div class="error-box">
bash: /usr/local/bin/script.sh: Permission denied
            </div>
            <div class="solution-box">
                <strong>解決策：</strong><br>
                $ chmod +x /usr/local/bin/script.sh  # 実行権限を付与<br>
                $ sudo コマンド  # または管理者権限で実行
            </div>
        </div>
        
        <div class="explanation">
            <h3>エラー2: Command not found</h3>
            <div class="error-box">
bash: nginx: command not found
            </div>
            <div class="solution-box">
                <strong>解決策：</strong><br>
                $ which nginx  # パスを確認<br>
                $ apt install nginx  # パッケージをインストール<br>
                $ export PATH=$PATH:/usr/sbin  # PATHに追加
            </div>
        </div>
        
        <div class="explanation">
            <h3>エラー3: Port already in use</h3>
            <div class="error-box">
bind() to 0.0.0.0:80 failed (98: Address already in use)
            </div>
            <div class="solution-box">
                <strong>解決策：</strong><br>
                $ sudo lsof -i :80  # 80番ポートを使用中のプロセスを確認<br>
                $ sudo kill -9 PID  # 該当プロセスを終了<br>
                # または別のポートに変更
            </div>
        </div>
        
        <div class="explanation">
            <h3>エラー4: No space left on device</h3>
            <div class="error-box">
cannot create regular file: No space left on device
            </div>
            <div class="solution-box">
                <strong>解決策：</strong><br>
                $ df -h  # ディスク使用状況を確認<br>
                $ du -sh /*  # 各ディレクトリのサイズ確認<br>
                $ sudo apt autoremove  # 不要パッケージ削除<br>
                $ sudo journalctl --vacuum-size=100M  # ログ削減
            </div>
        </div>
        
        <h2>5.4 実践的なデバッグ手法</h2>
        
        <div class="key-point">
            <strong>デバッグの基本手順：</strong>
            <ol>
                <li><strong>エラーメッセージを読む</strong> - 最初の手がかり</li>
                <li><strong>ログを確認</strong> - /var/log/ や journalctl</li>
                <li><strong>設定ファイルを確認</strong> - 文法エラーやタイポ</li>
                <li><strong>権限を確認</strong> - ls -la でファイル権限確認</li>
                <li><strong>プロセス状態を確認</strong> - ps, top, htop</li>
                <li><strong>ネットワークを確認</strong> - ping, curl, netstat</li>
                <li><strong>リソースを確認</strong> - df, free, iostat</li>
            </ol>
        </div>
        
        <div class="exercise-box">
            <h3>演習2: トラブルシューティング練習</h3>
            
            <p><strong>シナリオ：</strong>Nginxを起動したが、ブラウザでアクセスできない</p>
            
            <div class="command-box">
# 1. サービス状態確認<br>
$ systemctl status nginx<br><br>

# 2. ポート確認<br>
$ sudo netstat -tuln | grep :80<br><br>

# 3. ファイアウォール確認<br>
$ sudo ufw status<br><br>

# 4. ログ確認<br>
$ sudo tail -f /var/log/nginx/error.log<br><br>

# 5. 設定ファイル文法チェック<br>
$ sudo nginx -t<br><br>

# 6. curlでローカルテスト<br>
$ curl http://localhost
            </div>
        </div>
        
        <div class="explanation">
            <strong>覚えておくべき重要コマンド：</strong>
            <ul>
                <li><code>systemctl status/start/stop/restart</code> - サービス管理</li>
                <li><code>journalctl -xe</code> - システムログ確認</li>
                <li><code>tail -f /var/log/xxx</code> - ログのリアルタイム監視</li>
                <li><code>lsof -i :ポート番号</code> - ポート使用プロセス確認</li>
                <li><code>strace コマンド</code> - システムコール追跡</li>
                <li><code>tcpdump</code> - パケットキャプチャ</li>
            </ul>
        </div>
    </div>
</body>
</html>