---
layout: chapter
title: "付録：コマンド一覧表"
chapter: appendix
---

<div class="section">
    <h1>付録：コマンド一覧表</h1>
    
    <h2>基本コマンド</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>ls</code></td>
                <td>ファイル一覧</td>
                <td>-l, -a, -h</td>
                <td><code>ls -la</code></td>
            </tr>
            <tr>
                <td><code>cd</code></td>
                <td>ディレクトリ移動</td>
                <td>~, .., -</td>
                <td><code>cd ~/Documents</code></td>
            </tr>
            <tr>
                <td><code>pwd</code></td>
                <td>現在位置表示</td>
                <td>-</td>
                <td><code>pwd</code></td>
            </tr>
            <tr>
                <td><code>mkdir</code></td>
                <td>ディレクトリ作成</td>
                <td>-p</td>
                <td><code>mkdir -p dir1/dir2</code></td>
            </tr>
            <tr>
                <td><code>rmdir</code></td>
                <td>空ディレクトリ削除</td>
                <td>-p</td>
                <td><code>rmdir emptydir</code></td>
            </tr>
            <tr>
                <td><code>rm</code></td>
                <td>ファイル・ディレクトリ削除</td>
                <td>-r (ディレクトリ削除), -i (確認削除)</td>
                <td><code>rm -r directory</code></td>
            </tr>
            <tr>
                <td><code>cp</code></td>
                <td>コピー</td>
                <td>-r, -p</td>
                <td><code>cp -r src dest</code></td>
            </tr>
            <tr>
                <td><code>mv</code></td>
                <td>移動・名前変更</td>
                <td>-</td>
                <td><code>mv old.txt new.txt</code></td>
            </tr>
        </tbody>
    </table>
    
    <h2>ファイル操作・表示</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>cat</code></td>
                <td>ファイル内容表示</td>
                <td>-n</td>
                <td><code>cat -n file.txt</code></td>
            </tr>
            <tr>
                <td><code>less</code></td>
                <td>ページ単位表示</td>
                <td>-S</td>
                <td><code>less file.txt</code></td>
            </tr>
            <tr>
                <td><code>head</code></td>
                <td>先頭行表示</td>
                <td>-n</td>
                <td><code>head -10 file.txt</code></td>
            </tr>
            <tr>
                <td><code>tail</code></td>
                <td>末尾行表示</td>
                <td>-n, -f</td>
                <td><code>tail -f /var/log/syslog</code><br><code>tail -f /var/log/messages</code></td>
            </tr>
            <tr>
                <td><code>grep</code></td>
                <td>文字列検索</td>
                <td>-i, -r, -v</td>
                <td><code>grep -r "error" /var/log</code></td>
            </tr>
            <tr>
                <td><code>find</code></td>
                <td>ファイル検索</td>
                <td>-name, -type</td>
                <td><code>find . -name "*.txt"</code></td>
            </tr>
            <tr>
                <td><code>wc</code></td>
                <td>行数・文字数カウント</td>
                <td>-l, -w, -c</td>
                <td><code>wc -l file.txt</code></td>
            </tr>
            <tr>
                <td><code>sort</code></td>
                <td>並び替え</td>
                <td>-r, -n</td>
                <td><code>sort -n numbers.txt</code></td>
            </tr>
        </tbody>
    </table>

    <div class="key-point">
        <strong>補足：</strong>ログのパスはディストリビューションで異なります（例: Debian/Ubuntuは <code>/var/log/syslog</code>、RHEL系は <code>/var/log/messages</code>）。systemd環境では <code>journalctl</code> でも確認できます。
    </div>
    
    <h2>権限・所有者</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>chmod</code></td>
                <td>権限変更</td>
                <td>-R</td>
                <td><code>chmod 755 file.sh</code></td>
            </tr>
            <tr>
                <td><code>chown</code></td>
                <td>所有者変更</td>
                <td>-R</td>
                <td><code>chown user:group file</code></td>
            </tr>
            <tr>
                <td><code>umask</code></td>
                <td>デフォルト権限設定</td>
                <td>-</td>
                <td><code>umask 022</code></td>
            </tr>
        </tbody>
    </table>
    
    <h2>プロセス管理</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>ps</code></td>
                <td>プロセス一覧</td>
                <td>aux, -ef</td>
                <td><code>ps aux</code></td>
            </tr>
            <tr>
                <td><code>top</code></td>
                <td>リアルタイム監視</td>
                <td>-</td>
                <td><code>top</code></td>
            </tr>
            <tr>
                <td><code>htop</code></td>
                <td>高機能なtop</td>
                <td>-</td>
                <td><code>htop</code></td>
            </tr>
	            <tr>
	                <td><code>kill</code></td>
	                <td>プロセス終了</td>
	                <td>-TERM（既定）, -KILL</td>
	                <td><code>kill -TERM 1234</code></td>
	            </tr>
            <tr>
                <td><code>killall</code></td>
                <td>プロセス名で終了</td>
                <td>-TERM（既定）, -KILL</td>
                <td><code>killall firefox</code></td>
            </tr>
            <tr>
                <td><code>jobs</code></td>
                <td>ジョブ一覧</td>
                <td>-</td>
                <td><code>jobs</code></td>
            </tr>
            <tr>
                <td><code>nohup</code></td>
                <td>ログアウト後も実行</td>
                <td>-</td>
                <td><code>nohup command &</code></td>
            </tr>
        </tbody>
    </table>
    
    <h2>ネットワーク</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>ping</code></td>
                <td>疎通確認</td>
                <td>-c</td>
                <td><code>ping -c 4 example.com</code></td>
            </tr>
            <tr>
                <td><code>curl</code></td>
                <td>HTTP通信</td>
                <td>-I, -o</td>
                <td><code>curl -I https://example.com</code></td>
            </tr>
            <tr>
                <td><code>wget</code></td>
                <td>ファイルダウンロード</td>
                <td>-O</td>
                <td><code>wget -O file.zip https://example.com/file.zip</code></td>
            </tr>
            <tr>
                <td><code>netstat</code></td>
                <td>接続状況</td>
                <td>-tuln, -r</td>
                <td><code>netstat -tuln</code></td>
            </tr>
            <tr>
                <td><code>ss</code></td>
                <td>ソケット統計</td>
                <td>-tuln</td>
                <td><code>ss -tuln</code></td>
            </tr>
            <tr>
                <td><code>nslookup</code></td>
                <td>DNS問い合わせ</td>
                <td>-</td>
                <td><code>nslookup example.com</code></td>
            </tr>
            <tr>
                <td><code>dig</code></td>
                <td>DNS詳細問い合わせ</td>
                <td>+short</td>
                <td><code>dig +short example.com</code></td>
            </tr>
        </tbody>
    </table>
    
    <h2>システム情報</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>uname</code></td>
                <td>システム情報</td>
                <td>-a</td>
                <td><code>uname -a</code></td>
            </tr>
            <tr>
                <td><code>df</code></td>
                <td>ディスク使用量</td>
                <td>-h</td>
                <td><code>df -h</code></td>
            </tr>
            <tr>
                <td><code>du</code></td>
                <td>ディレクトリ使用量</td>
                <td>-sh</td>
                <td><code>du -sh /var/log</code></td>
            </tr>
            <tr>
                <td><code>free</code></td>
                <td>メモリ使用量</td>
                <td>-h</td>
                <td><code>free -h</code></td>
            </tr>
            <tr>
                <td><code>uptime</code></td>
                <td>稼働時間・負荷</td>
                <td>-</td>
                <td><code>uptime</code></td>
            </tr>
            <tr>
                <td><code>who</code></td>
                <td>ログインユーザー</td>
                <td>-</td>
                <td><code>who</code></td>
            </tr>
            <tr>
                <td><code>id</code></td>
                <td>ユーザーID確認</td>
                <td>-</td>
                <td><code>id</code></td>
            </tr>
        </tbody>
    </table>
    
    <h2>アーカイブ・圧縮</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>コマンド</th>
                <th>用途</th>
                <th>主要オプション</th>
                <th>使用例</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>tar</code></td>
                <td>アーカイブ作成・展開</td>
                <td>-czf, -xzf</td>
                <td><code>tar -czf backup.tar.gz /home</code></td>
            </tr>
            <tr>
                <td><code>zip</code></td>
                <td>ZIP圧縮</td>
                <td>-r</td>
                <td><code>zip -r archive.zip folder</code></td>
            </tr>
            <tr>
                <td><code>unzip</code></td>
                <td>ZIP展開</td>
                <td>-d</td>
                <td><code>unzip archive.zip -d /tmp</code></td>
            </tr>
            <tr>
                <td><code>gzip</code></td>
                <td>gzip圧縮</td>
                <td>-d</td>
                <td><code>gzip file.txt</code></td>
            </tr>
            <tr>
                <td><code>gunzip</code></td>
                <td>gzip展開</td>
                <td>-</td>
                <td><code>gunzip file.txt.gz</code></td>
            </tr>
        </tbody>
    </table>
    
    <div class="key-point">
        <strong>よく使う記号・特殊文字</strong>
        <ul>
            <li><code>|</code> - パイプ（コマンドの出力を次のコマンドの入力に）</li>
            <li><code>></code> - リダイレクト（出力をファイルに保存・上書き）</li>
            <li><code>>></code> - 追記リダイレクト（出力をファイルに追記）</li>
            <li><code>&</code> - バックグラウンド実行</li>
            <li><code>&&</code> - 前のコマンドが成功したら次を実行</li>
            <li><code>||</code> - 前のコマンドが失敗したら次を実行</li>
            <li><code>*</code> - ワイルドカード（任意の文字列）</li>
            <li><code>?</code> - ワイルドカード（任意の1文字）</li>
            <li><code>~</code> - ホームディレクトリ</li>
            <li><code>.</code> - 現在のディレクトリ</li>
            <li><code>..</code> - 親ディレクトリ</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>目次へ：</strong><a href="../">目次</a>に戻り、必要な章を参照してください。
    </div>
</div>
