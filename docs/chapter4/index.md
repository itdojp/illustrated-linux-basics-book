---
layout: chapter
title: "第4章：よくあるエラーと対処法"
chapter: 4
---

<div class="section">
    <h1>第4章：よくあるエラーと対処法</h1>
    
    <h2>4.0 この章で学ぶこと</h2>
    
    <div class="explanation">
        <ul>
            <li>よくあるエラーの「原因の当たり」を付けられる</li>
            <li>エラーメッセージから次に取るべき行動を判断できる</li>
            <li>トラブルシューティング用コマンドで状況を確認できる</li>
        </ul>
    </div>
    
    <h2>4.1 初心者が必ず遭遇するエラー TOP 10</h2>
    
    <div class="diagram-container">
        <svg width="850" height="600" viewBox="0 0 850 600">
            <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">Linux エラーメッセージ診断チャート</text>
            
            <!-- Permission denied -->
            <g transform="translate(50, 60)">
                <rect x="0" y="0" width="350" height="100" fill="#e74c3c" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">1. Permission denied</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">権限がありません</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: sudo を使う</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">または chmod で権限変更</text>
            </g>
            
            <!-- Command not found -->
            <g transform="translate(450, 60)">
                <rect x="0" y="0" width="350" height="100" fill="#3498db" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">2. Command not found</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">コマンドが見つかりません</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: apt/yum でインストール</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">またはPATHを確認</text>
            </g>
            
            <!-- No such file or directory -->
            <g transform="translate(50, 180)">
                <rect x="0" y="0" width="350" height="100" fill="#f39c12" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">3. No such file or directory</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">ファイルが存在しません</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: パスを確認</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">pwd と ls で現在地確認</text>
            </g>
            
            <!-- Is a directory -->
            <g transform="translate(450, 180)">
                <rect x="0" y="0" width="350" height="100" fill="#9b59b6" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">4. Is a directory</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">ディレクトリです（ファイルではない）</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: cd でディレクトリに移動</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">または正しいファイル名を指定</text>
            </g>
            
            <!-- Device or resource busy -->
            <g transform="translate(50, 300)">
                <rect x="0" y="0" width="350" height="100" fill="#1abc9c" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">5. Device or resource busy</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">使用中のため操作できません</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: lsof でプロセス確認</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">必要なら kill で終了</text>
            </g>
            
            <!-- No space left on device -->
            <g transform="translate(450, 300)">
                <rect x="0" y="0" width="350" height="100" fill="#e67e22" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">6. No space left on device</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">ディスク容量不足</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: df -h で容量確認</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">不要ファイルを削除</text>
            </g>
            
            <!-- Connection refused -->
            <g transform="translate(50, 420)">
                <rect x="0" y="0" width="350" height="100" fill="#34495e" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">7. Connection refused</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">接続が拒否されました</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: サービスが起動しているか確認</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">systemctl status でチェック</text>
            </g>
            
            <!-- Syntax error -->
            <g transform="translate(450, 420)">
                <rect x="0" y="0" width="350" height="100" fill="#2ecc71" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">8. Syntax error</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">構文エラー</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: スペルミスや記号を確認</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">特にスペースや引用符に注意</text>
            </g>
        </svg>
    </div>
    
    <h2>4.2 エラー別対処法詳細</h2>
    
    <div class="command-grid">
        <div class="command-card error-card">
            <h3>🚫 Permission denied</h3>
            <div class="error-box">bash: /etc/hosts: Permission denied</div>
            <h4>原因：</h4>
            <p>ファイルやディレクトリへのアクセス権限がない</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ sudo nano /etc/hosts  # 管理者権限で実行<br>
$ ls -l file.txt  # 権限を確認<br>
$ chmod 644 file.txt  # 権限を変更<br>
$ sudo chown $USER file.txt  # 所有者を変更
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>❓ Command not found</h3>
            <div class="error-box">git: command not found</div>
            <h4>原因：</h4>
            <p>コマンドがインストールされていない、またはPATHが通っていない</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ sudo apt install git  # Ubuntu/Debian<br>
$ sudo yum install git  # CentOS/RHEL<br>
$ which git  # インストール確認<br>
$ echo $PATH  # PATH確認<br>
$ export PATH=$PATH:/new/path  # PATH追加
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>📁 No such file or directory</h3>
            <div class="error-box">cat: test.txt: No such file or directory</div>
            <h4>原因：</h4>
            <p>指定したファイルやディレクトリが存在しない</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ pwd  # 現在のディレクトリを確認<br>
$ ls  # ファイル一覧を確認<br>
$ ls -la  # 隠しファイルも含めて確認<br>
$ find . -name "test.txt"  # ファイルを検索
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>💾 No space left on device</h3>
            <div class="error-box">cp: error writing './large.file': No space left on device</div>
            <h4>原因：</h4>
            <p>ディスクの空き容量が不足</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ df -h  # ディスク使用状況確認<br>
$ du -sh *  # 各ディレクトリのサイズ確認<br>
$ sudo apt autoremove  # 不要パッケージ削除<br>
$ sudo apt clean  # キャッシュクリア<br>
$ find /tmp -type f -delete  # /tmp クリーンアップ
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>🔒 Device or resource busy</h3>
            <div class="error-box">umount: /mnt: target is busy</div>
            <h4>原因：</h4>
            <p>ファイルやディレクトリが使用中</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ lsof /mnt  # 使用中のプロセスを確認<br>
$ fuser -v /mnt  # 使用中のプロセスを表示<br>
$ cd /  # ディレクトリから移動<br>
$ sudo umount -l /mnt  # 強制アンマウント
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>🌐 Connection refused</h3>
            <div class="error-box">curl: (7) Failed to connect to localhost port 80: Connection refused</div>
            <h4>原因：</h4>
            <p>サービスが起動していない、またはポートが閉じている</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ sudo systemctl status apache2  # サービス状態確認<br>
$ sudo systemctl start apache2  # サービス起動<br>
$ sudo netstat -tlnp  # ポート確認<br>
$ sudo ufw status  # ファイアウォール確認<br>
$ sudo ufw allow 80  # ポート開放
            </div>
        </div>
    </div>
    
    <h2>4.3 エラーメッセージの読み方</h2>
    
    <div class="explanation">
        <h3>エラーメッセージの構造</h3>
        <div class="error-box">bash: /usr/bin/foo: No such file or directory</div>
        <p>👆 この例を分解すると：</p>
        <ul>
            <li><strong>bash:</strong> エラーを出したプログラム</li>
            <li><strong>/usr/bin/foo:</strong> 問題のあるファイルやコマンド</li>
            <li><strong>No such file or directory:</strong> エラーの内容</li>
        </ul>
        
        <h3>デバッグのコツ</h3>
        <ol>
            <li><strong>エラーメッセージを最後まで読む</strong> - 重要な情報は最後にあることが多い</li>
            <li><strong>ファイル名やパスを確認</strong> - タイポが原因の場合が多い</li>
            <li><strong>権限を確認</strong> - <code>ls -l</code> で確認</li>
            <li><strong>ログファイルを見る</strong> - <code>/var/log/</code> 以下のログを確認</li>
            <li><strong>エラーメッセージで検索</strong> - Google検索で解決策が見つかることが多い</li>
        </ol>
    </div>
    
    <h2>4.4 トラブルシューティングコマンド</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>システム情報確認</h3>
            <div class="command-box">
$ uname -a  # システム情報<br>
$ cat /etc/os-release  # OS情報<br>
$ free -h  # メモリ使用状況<br>
$ df -h  # ディスク使用状況<br>
$ top  # プロセス監視
            </div>
        </div>
        
        <div class="command-card">
            <h3>ログ確認</h3>
            <div class="command-box">
$ sudo tail -f /var/log/syslog  # システムログ<br>
$ sudo journalctl -xe  # systemdログ<br>
$ dmesg  # カーネルメッセージ<br>
$ last  # ログイン履歴
            </div>
        </div>
        
        <div class="command-card">
            <h3>ネットワーク診断</h3>
            <div class="command-box">
$ ping google.com  # 接続確認<br>
$ ip addr  # IPアドレス確認<br>
$ netstat -tlnp  # ポート確認<br>
$ ss -tlnp  # ソケット確認<br>
$ traceroute google.com  # 経路確認
            </div>
        </div>
    </div>
    
    <h2>4.5 よくある質問と回答</h2>
    
    <div class="faq-section">
        <h3>Q: sudoパスワードを忘れました</h3>
        <p>A: リカバリーモードで起動し、rootでログインしてパスワードをリセットします。</p>
        <div class="command-box">$ passwd username</div>
        
        <h3>Q: ファイルを誤って削除しました</h3>
        <p>A: Linuxでは通常、削除したファイルの復元は困難です。定期的なバックアップが重要です。</p>
        
        <h3>Q: システムが重い/遅い</h3>
        <p>A: topコマンドでCPU/メモリ使用率の高いプロセスを確認します。</p>
        <div class="command-box">$ top  # qで終了</div>
        
        <h3>Q: パッケージの依存関係エラー</h3>
        <p>A: パッケージマネージャーの修復コマンドを実行します。</p>
        <div class="command-box">
$ sudo apt --fix-broken install  # Ubuntu/Debian<br>
$ sudo yum-complete-transaction  # CentOS/RHEL
        </div>
    </div>
    
    <h2>4.6 まとめ</h2>
    
    <div class="explanation">
        <ul>
            <li>まずは「エラーメッセージを読む」→「何が無い/権限が無い/場所が違う」を切り分ける</li>
            <li>困ったら <code>top</code>/<code>df</code>/<code>journalctl</code> などで状況確認する</li>
            <li>再発防止には、手順の記録とバックアップが有効</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>次章予告：</strong>次章では、これまでのコマンドを組み合わせて簡単なシェルスクリプトを作り、定期実行まで試します。
    </div>
</div>
