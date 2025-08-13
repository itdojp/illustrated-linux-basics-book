---
layout: chapter
title: "付録：クイックリファレンス（チートシート）"
chapter: appendix
---
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>付録：クイックリファレンス（チートシート）</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.4;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .cheatsheet-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }
        .cheatsheet-header h1 {
            margin: 0;
            font-size: 32px;
        }
        .cheatsheet-header p {
            margin: 10px 0 0 0;
            opacity: 0.9;
        }
        .cheat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
        }
        .cheat-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            break-inside: avoid;
        }
        .cheat-card h2 {
            margin: 0 0 15px 0;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498db;
            color: #2c3e50;
            font-size: 18px;
        }
        .cheat-card h3 {
            margin: 15px 0 10px 0;
            color: #34495e;
            font-size: 14px;
            font-weight: bold;
        }
        .command-list {
            margin: 0;
            padding: 0;
        }
        .command-item {
            display: flex;
            margin: 8px 0;
            align-items: flex-start;
        }
        .cmd {
            background: #2c3e50;
            color: #27ae60;
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            white-space: nowrap;
            min-width: 140px;
        }
        .desc {
            margin-left: 10px;
            color: #7f8c8d;
            font-size: 12px;
            flex: 1;
        }
        .shortcut-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        .shortcut-table td {
            padding: 6px;
            border-bottom: 1px solid #ecf0f1;
        }
        .shortcut-table td:first-child {
            font-family: 'Courier New', monospace;
            background: #ecf0f1;
            font-weight: bold;
            width: 40%;
        }
        .permission-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin: 10px 0;
        }
        .permission-box {
            text-align: center;
            padding: 8px;
            background: #ecf0f1;
            border-radius: 4px;
        }
        .permission-box .num {
            font-size: 20px;
            font-weight: bold;
            color: #3498db;
        }
        .permission-box .meaning {
            font-size: 11px;
            color: #7f8c8d;
        }
        .port-list {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 5px;
            font-size: 12px;
        }
        .port-item {
            display: flex;
            align-items: center;
        }
        .port-num {
            background: #e74c3c;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            margin-right: 8px;
            font-family: monospace;
            font-weight: bold;
            min-width: 40px;
            text-align: center;
        }
        .emergency-box {
            background: #ffe5e5;
            border: 2px solid #e74c3c;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
        }
        .emergency-box h3 {
            color: #e74c3c;
            margin-top: 0;
        }
        @media print {
            .cheatsheet-header {
                background: #2c3e50 !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            .cheat-card {
                page-break-inside: avoid;
            }
        }
    </style>
</head>
<body>
    <div class="cheatsheet-header">
        <h1>🚀 Linux超入門 チートシート</h1>
        <p>よく使うコマンド・概念の早見表</p>
    </div>
    
    <div class="cheat-grid">
        <!-- ナビゲーション系 -->
        <div class="cheat-card">
            <h2>📁 ナビゲーション・ファイル操作</h2>
            
            <h3>移動・表示</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">pwd</span>
                    <span class="desc">現在のディレクトリ表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">ls -la</span>
                    <span class="desc">ファイル一覧（詳細・隠しファイル含む）</span>
                </div>
                <div class="command-item">
                    <span class="cmd">cd /path/to/dir</span>
                    <span class="desc">ディレクトリ移動</span>
                </div>
                <div class="command-item">
                    <span class="cmd">cd ..</span>
                    <span class="desc">親ディレクトリへ</span>
                </div>
                <div class="command-item">
                    <span class="cmd">cd ~</span>
                    <span class="desc">ホームディレクトリへ</span>
                </div>
            </div>
            
            <h3>ファイル・フォルダ操作</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">cp file1 file2</span>
                    <span class="desc">ファイルコピー</span>
                </div>
                <div class="command-item">
                    <span class="cmd">cp -r dir1 dir2</span>
                    <span class="desc">ディレクトリコピー</span>
                </div>
                <div class="command-item">
                    <span class="cmd">mv old new</span>
                    <span class="desc">移動/名前変更</span>
                </div>
                <div class="command-item">
                    <span class="cmd">rm file</span>
                    <span class="desc">ファイル削除</span>
                </div>
                <div class="command-item">
                    <span class="cmd">rm -rf dir</span>
                    <span class="desc">ディレクトリ強制削除</span>
                </div>
                <div class="command-item">
                    <span class="cmd">mkdir dirname</span>
                    <span class="desc">ディレクトリ作成</span>
                </div>
                <div class="command-item">
                    <span class="cmd">touch file</span>
                    <span class="desc">空ファイル作成</span>
                </div>
            </div>
        </div>
        
        <!-- ファイル内容系 -->
        <div class="cheat-card">
            <h2>📄 ファイル内容操作</h2>
            
            <h3>表示・検索</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">cat file</span>
                    <span class="desc">ファイル全体表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">less file</span>
                    <span class="desc">ページング表示（q で終了）</span>
                </div>
                <div class="command-item">
                    <span class="cmd">head -n 10 file</span>
                    <span class="desc">先頭10行表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">tail -n 10 file</span>
                    <span class="desc">末尾10行表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">tail -f file</span>
                    <span class="desc">リアルタイム監視</span>
                </div>
                <div class="command-item">
                    <span class="cmd">grep "text" file</span>
                    <span class="desc">文字列検索</span>
                </div>
                <div class="command-item">
                    <span class="cmd">grep -r "text" .</span>
                    <span class="desc">再帰的に検索</span>
                </div>
            </div>
            
            <h3>編集</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">nano file</span>
                    <span class="desc">簡単エディタ</span>
                </div>
                <div class="command-item">
                    <span class="cmd">vi file</span>
                    <span class="desc">viエディタ</span>
                </div>
                <div class="command-item">
                    <span class="cmd">echo "text" > file</span>
                    <span class="desc">上書き出力</span>
                </div>
                <div class="command-item">
                    <span class="cmd">echo "text" >> file</span>
                    <span class="desc">追記出力</span>
                </div>
            </div>
        </div>
        
        <!-- パーミッション -->
        <div class="cheat-card">
            <h2>🔐 パーミッション</h2>
            
            <h3>権限変更</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">chmod 755 file</span>
                    <span class="desc">rwxr-xr-x に設定</span>
                </div>
                <div class="command-item">
                    <span class="cmd">chmod +x file</span>
                    <span class="desc">実行権限追加</span>
                </div>
                <div class="command-item">
                    <span class="cmd">chmod -w file</span>
                    <span class="desc">書込権限削除</span>
                </div>
                <div class="command-item">
                    <span class="cmd">chown user:group file</span>
                    <span class="desc">所有者変更</span>
                </div>
            </div>
            
            <h3>数値表記</h3>
            <div class="permission-grid">
                <div class="permission-box">
                    <div class="num">4</div>
                    <div class="meaning">読み取り(r)</div>
                </div>
                <div class="permission-box">
                    <div class="num">2</div>
                    <div class="meaning">書き込み(w)</div>
                </div>
                <div class="permission-box">
                    <div class="num">1</div>
                    <div class="meaning">実行(x)</div>
                </div>
            </div>
            
            <h3>よく使う設定</h3>
            <table class="shortcut-table">
                <tr>
                    <td>755</td>
                    <td>rwxr-xr-x（プログラム）</td>
                </tr>
                <tr>
                    <td>644</td>
                    <td>rw-r--r--（通常ファイル）</td>
                </tr>
                <tr>
                    <td>600</td>
                    <td>rw-------（秘密鍵等）</td>
                </tr>
                <tr>
                    <td>777</td>
                    <td>rwxrwxrwx（全権限）</td>
                </tr>
            </table>
        </div>
        
        <!-- プロセス管理 -->
        <div class="cheat-card">
            <h2>⚙️ プロセス・サービス管理</h2>
            
            <h3>プロセス操作</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">ps aux</span>
                    <span class="desc">全プロセス表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">top</span>
                    <span class="desc">リアルタイム監視</span>
                </div>
                <div class="command-item">
                    <span class="cmd">htop</span>
                    <span class="desc">高機能監視ツール</span>
                </div>
                <div class="command-item">
                    <span class="cmd">kill PID</span>
                    <span class="desc">プロセス終了</span>
                </div>
                <div class="command-item">
                    <span class="cmd">kill -9 PID</span>
                    <span class="desc">強制終了</span>
                </div>
                <div class="command-item">
                    <span class="cmd">jobs</span>
                    <span class="desc">ジョブ一覧</span>
                </div>
                <div class="command-item">
                    <span class="cmd">command &</span>
                    <span class="desc">バックグラウンド実行</span>
                </div>
            </div>
            
            <h3>サービス管理（systemd）</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">systemctl start service</span>
                    <span class="desc">サービス起動</span>
                </div>
                <div class="command-item">
                    <span class="cmd">systemctl stop service</span>
                    <span class="desc">サービス停止</span>
                </div>
                <div class="command-item">
                    <span class="cmd">systemctl restart service</span>
                    <span class="desc">サービス再起動</span>
                </div>
                <div class="command-item">
                    <span class="cmd">systemctl status service</span>
                    <span class="desc">状態確認</span>
                </div>
                <div class="command-item">
                    <span class="cmd">systemctl enable service</span>
                    <span class="desc">自動起動有効</span>
                </div>
            </div>
        </div>
        
        <!-- ネットワーク -->
        <div class="cheat-card">
            <h2>🌐 ネットワーク</h2>
            
            <h3>接続確認</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">ping google.com</span>
                    <span class="desc">疎通確認</span>
                </div>
                <div class="command-item">
                    <span class="cmd">curl http://example.com</span>
                    <span class="desc">HTTPリクエスト</span>
                </div>
                <div class="command-item">
                    <span class="cmd">wget http://file.url</span>
                    <span class="desc">ファイルダウンロード</span>
                </div>
                <div class="command-item">
                    <span class="cmd">traceroute google.com</span>
                    <span class="desc">経路追跡</span>
                </div>
                <div class="command-item">
                    <span class="cmd">nslookup domain.com</span>
                    <span class="desc">DNS問合せ</span>
                </div>
            </div>
            
            <h3>状態確認</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">ip addr</span>
                    <span class="desc">IPアドレス確認</span>
                </div>
                <div class="command-item">
                    <span class="cmd">netstat -tuln</span>
                    <span class="desc">ポート状態確認</span>
                </div>
                <div class="command-item">
                    <span class="cmd">ss -tuln</span>
                    <span class="desc">ソケット状態（新）</span>
                </div>
                <div class="command-item">
                    <span class="cmd">lsof -i :80</span>
                    <span class="desc">ポート使用プロセス</span>
                </div>
            </div>
            
            <h3>主要ポート番号</h3>
            <div class="port-list">
                <div class="port-item">
                    <span class="port-num">22</span>
                    <span>SSH</span>
                </div>
                <div class="port-item">
                    <span class="port-num">80</span>
                    <span>HTTP</span>
                </div>
                <div class="port-item">
                    <span class="port-num">443</span>
                    <span>HTTPS</span>
                </div>
                <div class="port-item">
                    <span class="port-num">3306</span>
                    <span>MySQL</span>
                </div>
                <div class="port-item">
                    <span class="port-num">5432</span>
                    <span>PostgreSQL</span>
                </div>
                <div class="port-item">
                    <span class="port-num">6379</span>
                    <span>Redis</span>
                </div>
            </div>
        </div>
        
        <!-- Docker/コンテナ -->
        <div class="cheat-card">
            <h2>🐳 Docker基本コマンド</h2>
            
            <h3>イメージ操作</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">docker images</span>
                    <span class="desc">イメージ一覧</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker pull image:tag</span>
                    <span class="desc">イメージ取得</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker build -t name .</span>
                    <span class="desc">イメージビルド</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker rmi image</span>
                    <span class="desc">イメージ削除</span>
                </div>
            </div>
            
            <h3>コンテナ操作</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">docker run image</span>
                    <span class="desc">コンテナ起動</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker run -d image</span>
                    <span class="desc">バックグラウンド起動</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker run -p 8080:80 image</span>
                    <span class="desc">ポートマッピング</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker ps</span>
                    <span class="desc">実行中コンテナ</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker ps -a</span>
                    <span class="desc">全コンテナ表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker exec -it id bash</span>
                    <span class="desc">コンテナ内でbash</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker stop id</span>
                    <span class="desc">コンテナ停止</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker rm id</span>
                    <span class="desc">コンテナ削除</span>
                </div>
                <div class="command-item">
                    <span class="cmd">docker logs id</span>
                    <span class="desc">ログ確認</span>
                </div>
            </div>
        </div>
        
        <!-- システム情報 -->
        <div class="cheat-card">
            <h2>📊 システム情報・監視</h2>
            
            <h3>リソース確認</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">df -h</span>
                    <span class="desc">ディスク使用量</span>
                </div>
                <div class="command-item">
                    <span class="cmd">du -sh *</span>
                    <span class="desc">ディレクトリサイズ</span>
                </div>
                <div class="command-item">
                    <span class="cmd">free -h</span>
                    <span class="desc">メモリ使用量</span>
                </div>
                <div class="command-item">
                    <span class="cmd">uptime</span>
                    <span class="desc">稼働時間・負荷</span>
                </div>
                <div class="command-item">
                    <span class="cmd">uname -a</span>
                    <span class="desc">システム情報</span>
                </div>
            </div>
            
            <h3>ログ確認</h3>
            <div class="command-list">
                <div class="command-item">
                    <span class="cmd">journalctl -xe</span>
                    <span class="desc">システムログ（詳細）</span>
                </div>
                <div class="command-item">
                    <span class="cmd">journalctl -f</span>
                    <span class="desc">ログのリアルタイム表示</span>
                </div>
                <div class="command-item">
                    <span class="cmd">dmesg</span>
                    <span class="desc">カーネルメッセージ</span>
                </div>
                <div class="command-item">
                    <span class="cmd">/var/log/*</span>
                    <span class="desc">各種ログファイル</span>
                </div>
            </div>
        </div>
        
        <!-- ショートカット -->
        <div class="cheat-card">
            <h2>⌨️ 便利なショートカット</h2>
            
            <h3>ターミナル操作</h3>
            <table class="shortcut-table">
                <tr>
                    <td>Ctrl + C</td>
                    <td>実行中のコマンド中断</td>
                </tr>
                <tr>
                    <td>Ctrl + Z</td>
                    <td>プロセス一時停止</td>
                </tr>
                <tr>
                    <td>Ctrl + D</td>
                    <td>ログアウト/EOF</td>
                </tr>
                <tr>
                    <td>Ctrl + L</td>
                    <td>画面クリア</td>
                </tr>
                <tr>
                    <td>Ctrl + A</td>
                    <td>行頭へ移動</td>
                </tr>
                <tr>
                    <td>Ctrl + E</td>
                    <td>行末へ移動</td>
                </tr>
                <tr>
                    <td>Ctrl + R</td>
                    <td>履歴検索</td>
                </tr>
                <tr>
                    <td>Tab</td>
                    <td>自動補完</td>
                </tr>
                <tr>
                    <td>↑ / ↓</td>
                    <td>コマンド履歴</td>
                </tr>
            </table>
            
            <h3>特殊記号</h3>
            <table class="shortcut-table">
                <tr>
                    <td>|</td>
                    <td>パイプ（出力を次へ）</td>
                </tr>
                <tr>
                    <td>></td>
                    <td>リダイレクト（上書き）</td>
                </tr>
                <tr>
                    <td>>></td>
                    <td>リダイレクト（追記）</td>
                </tr>
                <tr>
                    <td>&</td>
                    <td>バックグラウンド実行</td>
                </tr>
                <tr>
                    <td>*</td>
                    <td>ワイルドカード</td>
                </tr>
                <tr>
                    <td>~</td>
                    <td>ホームディレクトリ</td>
                </tr>
                <tr>
                    <td>.</td>
                    <td>現在のディレクトリ</td>
                </tr>
                <tr>
                    <td>..</td>
                    <td>親ディレクトリ</td>
                </tr>
            </table>
        </div>
    </div>
    
    <!-- 緊急時対応 -->
    <div class="emergency-box">
        <h3>🚨 困ったときの緊急コマンド</h3>
        <div class="cheat-grid">
            <div>
                <strong>システムが重い時：</strong><br>
                <code>top</code> でプロセス確認 → <code>kill -9 PID</code> で強制終了
            </div>
            <div>
                <strong>ディスクが満杯：</strong><br>
                <code>df -h</code> で確認 → <code>du -sh /*</code> で原因特定 → 不要ファイル削除
            </div>
            <div>
                <strong>サービスが動かない：</strong><br>
                <code>systemctl status service</code> → <code>journalctl -xe</code> でエラー確認
            </div>
            <div>
                <strong>ネットワークに繋がらない：</strong><br>
                <code>ping 8.8.8.8</code> → <code>ip addr</code> → <code>systemctl restart network</code>
            </div>
            <div>
                <strong>権限エラー：</strong><br>
                <code>sudo</code> を付ける or <code>chmod</code> で権限変更
            </div>
            <div>
                <strong>コマンドが見つからない：</strong><br>
                <code>which command</code> → <code>apt install package</code> でインストール
            </div>
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 30px; color: #7f8c8d;">
        <p>📝 このチートシートは印刷して手元に置いておくと便利です</p>
        <p>更新日：2025年1月</p>
    </div>
</body>
</html>