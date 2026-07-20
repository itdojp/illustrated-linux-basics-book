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
            <li>よくあるエラーの原因の見当を付けられる</li>
            <li>エラーメッセージから次に取るべき行動を判断できる</li>
            <li>トラブルシューティング用コマンドで状況を確認できる</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>切り分けの基本：</strong>実務では「直前の変更」「再現性」「影響範囲」「ログ（いつ / どこで / 誰が）」「現在の状態（CPU / メモリ / ディスク / ネットワーク）」を整理すると、対応が速くなります。
    </div>
    
    <h2>4.1 初心者が遭遇しやすいエラー TOP 8</h2>
    
    <div class="diagram-container">
        <svg width="850" height="600" viewBox="0 0 850 600">
            <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">Linux エラーメッセージ診断チャート</text>
            
            <!-- Permission denied -->
            <g transform="translate(50, 60)">
                <rect x="0" y="0" width="350" height="100" fill="#e74c3c" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">1. Permission denied</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">権限がありません</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">確認: id / ls -l / namei -l</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">必要な権限と正規手順を確認</text>
            </g>
            
            <!-- Command not found -->
            <g transform="translate(450, 60)">
                <rect x="0" y="0" width="350" height="100" fill="#3498db" rx="10"/>
                <text x="175" y="30" text-anchor="middle" fill="white" font-size="16" font-weight="bold">2. Command not found</text>
                <text x="175" y="50" text-anchor="middle" fill="white" font-size="12">コマンドが見つかりません</text>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="14">解決: apt / yum / dnf でインストール</text>
                <text x="175" y="95" text-anchor="middle" fill="white" font-size="14">または PATH を確認</text>
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
            <h3>Permission denied</h3>
            <div class="error-box">bash: /etc/hosts: Permission denied</div>
            <h4>原因：</h4>
            <p>対象ファイルだけでなく、親ディレクトリの探索権限、所有者、読み取り専用マウント、セキュリティポリシー等が原因になる場合があります。</p>
            <h4>確認と対処：</h4>
            <div class="command-box">
$ id  # 自分のユーザーと所属グループを確認<br>
$ ls -l /etc/hosts  # 対象の所有者と権限を確認<br>
$ namei -l /etc/hosts  # 親ディレクトリを含めて確認<br>
$ chmod u+rw file.txt  # 自分が所有する練習用ファイルで、必要な権限だけを追加<br>
$ sudoedit /etc/hosts  # 管理対象ファイルは許可された手順で編集
            </div>
            <p><strong>注意：</strong>原因を確認せずに <code>sudo</code> を付けたり、<code>chmod 777</code> や <code>chown -R</code> を実行したりしないでください。共有環境や管理対象ファイルでは、管理者と運用手順を確認します。</p>
        </div>
        
        <div class="command-card error-card">
            <h3 id="path-placeholder-example">Command not found</h3>
            <div class="error-box">git: command not found</div>
            <h4>原因：</h4>
            <p>コマンドがインストールされていない、または PATH が通っていない</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ sudo apt install git  # Ubuntu/Debian<br>
$ sudo yum install git  # CentOS/RHEL<br>
$ sudo dnf install git  # Fedora/RHEL8+<br>
$ which git  # インストール確認<br>
$ echo $PATH  # PATH 確認<br>
$ export PATH="$PATH:&lt;directory-path&gt;"  # 例: &lt;directory-path&gt; を /opt/bin へ置換
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>No such file or directory</h3>
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
            <h3>Is a directory</h3>
            <div class="error-box">cat: mydir: Is a directory</div>
            <h4>原因：</h4>
            <p>ディレクトリをファイルとして扱おうとした（例: <code>cat</code> や <code>cp</code> の引数にディレクトリを指定）</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ ls -la mydir  # 種類（ファイル/ディレクトリ）を確認<br>
$ cd mydir  # ディレクトリなら移動して中身を見る<br>
$ ls -la  # 中のファイルを確認して正しいファイル名を指定
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>No space left on device</h3>
            <div class="error-box">cp: error writing './large.file': No space left on device</div>
            <h4>原因：</h4>
            <p>ディスクの空き容量が不足</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ df -h  # ディスク使用状況確認<br>
$ du -sh *  # 各ディレクトリのサイズ確認<br>
$ sudo apt autoremove  # 不要パッケージ削除<br>
$ sudo apt clean  # キャッシュクリア<br>
$ find /tmp -type f -mtime +7 -print  # 例: 7日より古いファイルをまず確認<br>
$ find /tmp -type f -mtime +7 -delete  # 確認後に削除（慎重に）
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>Device or resource busy</h3>
            <div class="error-box">umount: /mnt: target is busy</div>
            <h4>原因：</h4>
            <p>ファイルやディレクトリが使用中</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ lsof /mnt  # 使用中のプロセスを確認<br>
$ fuser -v /mnt  # 使用中のプロセスを表示<br>
$ cd /  # ディレクトリから移動<br>
$ sudo umount /mnt  # 通常のアンマウント<br>
$ sudo umount -l /mnt  # 最終手段（遅延アンマウント）
            </div>
        </div>
        
        <div class="command-card error-card">
            <h3>Connection refused</h3>
            <div class="error-box">curl: (7) Failed to connect to localhost port 80: Connection refused</div>
            <h4>原因：</h4>
            <p>サービスが起動していない、またはポートが閉じている</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ sudo systemctl status apache2  # Debian/Ubuntu<br>
$ sudo systemctl status httpd  # RHEL 系<br>
$ sudo systemctl start apache2  # Debian/Ubuntu<br>
$ sudo systemctl start httpd  # RHEL 系<br>
$ sudo ss -tlnp  # ポート確認<br>
$ sudo ufw status  # Debian/Ubuntu（UFW）<br>
$ sudo firewall-cmd --state  # RHEL 系（firewalld）<br>
$ sudo ufw allow 80/tcp  # Debian/Ubuntu<br>
$ sudo firewall-cmd --permanent --add-service=http && sudo firewall-cmd --reload  # RHEL 系
            </div>
        </div>

        <div class="command-card error-card">
            <h3>Syntax error</h3>
            <div class="error-box">bash: syntax error near unexpected token `then'</div>
            <h4>原因：</h4>
            <p>スペルミス、引用符（<code>'</code> / <code>"</code>）の閉じ忘れ、<code>if</code> / <code>fi</code> の対応漏れなど</p>
            <h4>解決方法：</h4>
            <div class="command-box">
$ bash -n script.sh  # 実行せず構文だけチェック<br>
$ nl -ba script.sh | sed -n '1,120p'  # 行番号付きで該当箇所を確認
            </div>
        </div>
    </div>
    
    <h2>4.3 エラーメッセージの読み方</h2>
    
    <div class="explanation">
        <h3>エラーメッセージの構造</h3>
        <div class="error-box">bash: /usr/bin/foo: No such file or directory</div>
        <p>この例を分解すると：</p>
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
            <li><strong>エラーメッセージで検索</strong> - Web 検索や公式ドキュメントで情報を確認する</li>
        </ol>
    </div>
    
    <h2>4.4 トラブルシューティングコマンド</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>システム情報確認</h3>
            <div class="command-box">
$ uname -a  # システム情報<br>
$ cat /etc/os-release  # OS 情報<br>
$ free -h  # メモリ使用状況<br>
$ df -h  # ディスク使用状況<br>
$ top  # プロセス監視
            </div>
        </div>
        
        <div class="command-card">
            <h3>ログ確認</h3>
            <div class="command-box">
$ sudo tail -f /var/log/syslog  # システムログ（Debian/Ubuntu）<br>
$ sudo tail -f /var/log/messages  # システムログ（RHEL 系）<br>
$ sudo journalctl -xe  # systemd ログ<br>
$ dmesg  # カーネルメッセージ<br>
$ last  # ログイン履歴
            </div>
        </div>
        
        <div class="command-card">
            <h3>ネットワーク診断</h3>
            <div class="command-box">
$ ping -c 4 1.1.1.1  # 接続確認（環境により ICMP が遮断されることがある）<br>
$ ip addr  # IP アドレス確認<br>
$ ss -tlnp  # ソケット / ポート確認<br>
$ netstat -tlnp  # ポート確認（net-tools）<br>
$ traceroute 1.1.1.1  # 経路確認（環境により UDP / ICMP が遮断されることがある）
            </div>
        </div>
    </div>
    
    <h2>4.5 よくある質問と回答</h2>
    
    <div class="faq-section">
        <h3>Q: sudo で求められるパスワードを忘れました</h3>
        <p>A: 多くの環境では、<code>sudo</code> で求められるのは自分のログインパスワードであり、専用の「sudo パスワード」ではありません。思い出せない場合は、許可された手順でリカバリーモード等から再設定するか、管理者に依頼します。</p>
        <div class="command-box"># passwd &lt;user-name&gt;  # リカバリーモードのrootシェルまたは管理者が実行</div>
        
        <h3>Q: ファイルを誤って削除しました</h3>
        <p>A: Linux では通常、削除したファイルの復元は困難です。まずはバックアップ / スナップショットの有無を確認し、再発防止として定期的なバックアップを運用します。</p>
        
        <h3>Q: システムが重い/遅い</h3>
        <p>A: <code>top</code> コマンドで CPU / メモリ使用率の高いプロセスを確認します。</p>
        <div class="command-box">$ top  # qで終了</div>
        
        <h3 id="dnf-recovery">Q: パッケージ管理で依存関係やトランザクションのエラーが出ました</h3>
        <p>A: ディストリビューションと症状を特定し、パッケージを変更しない確認から始めます。Ubuntu/Debianでは<code>apt --fix-broken install</code>の実行内容を確認します。RHEL 8/9・Fedora等のDNF系では、次の順で切り分けます。</p>
        <div class="command-box">
$ cat /etc/os-release  # distributionとversion<br>
$ dnf --version  # DNF世代<br>
$ dnf check  # インストール済みパッケージDBを検査（パッケージ変更なし）<br>
$ dnf history list  # トランザクションの成功・中止を確認（パッケージ変更なし）<br>
$ dnf history info &lt;transaction-id&gt;  # 対象の詳細（パッケージ変更なし）
        </div>
        <ul>
            <li><strong>インストール済みRPMの不整合：</strong><code>dnf check</code>の対象パッケージと問題種別を記録し、ベンダー手順または管理者判断へ渡します。</li>
            <li><strong>中断したトランザクション：</strong><code>dnf history list</code>でIDと結果を確認します。<code>history undo</code>や<code>rollback</code>はパッケージの削除・downgradeを伴い、旧バージョンがなければ失敗するため、一般的な修復として実行しません。</li>
            <li><strong>リポジトリメタデータ：</strong>リポジトリ設定・subscription・networkを確認後、<code>sudo dnf clean metadata</code>と<code>sudo dnf makecache</code>でメタデータcacheだけを再作成します。インストール済みパッケージは変更しません。</li>
            <li><strong>リポジトリとのバージョン差：</strong><code>sudo dnf --assumeno distro-sync</code>で候補を事前確認します。パッケージ指定がなければ全インストール済みパッケージが対象で、実行時はupgradeまたはdowngradeが起こり得ます。期待するリポジトリ・パッケージ・保守時間・バックアップを確認できるまで承認しません。</li>
        </ul>
        <p>旧YUMの<code>yum-complete-transaction</code>は、電源断やクラッシュで中断した旧YUMトランザクションを再開する専用ツールです。依存関係エラー一般の解決策でも、RHEL 8/9のDNF基本導線でもありません。根拠と確認日は<a href="../appendix/#dnf-source-notes">付録のDNF/YUM Source Notes</a>を参照してください。</p>
    </div>
    
    <h2>4.6 まとめ</h2>
    
    <div class="explanation">
        <ul>
            <li>まずはエラーメッセージを読み、「存在しない」「権限不足」「場所が違う」などを切り分ける</li>
            <li>必要に応じて <code>top</code> / <code>df</code> / <code>journalctl</code> などで状況を確認する</li>
            <li>再発防止には、手順の記録とバックアップが有効</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>次章予告：</strong>次章では、これまでのコマンドを組み合わせて簡単なシェルスクリプトを作成し、定期実行まで扱います。
    </div>
</div>
