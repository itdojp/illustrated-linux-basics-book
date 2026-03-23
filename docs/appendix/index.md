---
layout: chapter
title: "付録：コマンド一覧・用語集・参考リンク"
chapter: appendix
---

<div class="section">
    <h1>付録：コマンド一覧・用語集・参考リンク</h1>

    <div class="key-point">
        <strong>この付録の使い方：</strong>
        <ul>
            <li><a href="#command-reference">コマンド一覧</a> - 基本操作を素早く引き直す</li>
            <li><a href="#glossary">最小用語集</a> - 権限やプロセスなどの用語を確認する</li>
            <li><a href="#official-references">参考リンク</a> - <code>man</code> と公式ドキュメントをたどる</li>
        </ul>
    </div>
    
    <h2 id="command-reference">基本コマンド</h2>
    
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
                <td><code>ping -c 4 1.1.1.1</code></td>
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

    <h2 id="glossary">最小用語集</h2>

    <table class="comparison-table">
        <thead>
            <tr>
                <th>用語</th>
                <th>意味</th>
                <th>最初に出てくる章の目安</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>シェル</td>
                <td>コマンドを受け取り、OSへ処理を依頼するプログラム。代表例は <code>bash</code>。</td>
                <td>第1章</td>
            </tr>
            <tr>
                <td>ディストリビューション</td>
                <td>Linux カーネルに各種ソフトウェアや管理方針を組み合わせた配布形態。Ubuntu や RHEL 系など。</td>
                <td>第0章 / 第3章</td>
            </tr>
            <tr>
                <td>パッケージマネージャー</td>
                <td>ソフトウェアのインストール、更新、削除をまとめて管理する仕組み。<code>apt</code>、<code>dnf</code>、<code>yum</code> など。</td>
                <td>第3章</td>
            </tr>
            <tr>
                <td>プロセス</td>
                <td>実行中のプログラム。1つのコマンドやサービスが動作すると、OS上ではプロセスとして管理される。</td>
                <td>第1章 / 第4章</td>
            </tr>
            <tr>
                <td>PID</td>
                <td>各プロセスに付与される識別番号。<code>ps</code> や <code>top</code> で確認し、<code>kill</code> の対象にする。</td>
                <td>第1章</td>
            </tr>
            <tr>
                <td>root</td>
                <td>Linux の管理者権限を持つ特別なユーザー。操作範囲が広いため、日常作業での常用は避ける。</td>
                <td>第2章 / 第4章</td>
            </tr>
            <tr>
                <td>sudo</td>
                <td>必要な場面だけ一時的に管理者権限でコマンドを実行する仕組み。</td>
                <td>第2章 / 第4章</td>
            </tr>
            <tr>
                <td>権限（r/w/x）</td>
                <td>読み取り、書き込み、実行の可否を表す基本ルール。所有者、グループ、その他で別々に設定する。</td>
                <td>第2章</td>
            </tr>
            <tr>
                <td>ホームディレクトリ</td>
                <td>各ユーザーの作業開始地点。通常は <code>~</code> で表す。</td>
                <td>第1章</td>
            </tr>
            <tr>
                <td>標準入力 / 標準出力</td>
                <td>コマンドが受け取る入力と、画面やファイルへ出す結果。パイプやリダイレクトの理解に必要。</td>
                <td>第1章 / 第3章</td>
            </tr>
        </tbody>
    </table>

    <h2 id="official-references">さらに確認したいときの参照先</h2>

    <div class="explanation">
        <h3>まずは <code>man</code> を引く</h3>
        <ul>
            <li><code>man 1 ls</code> - コマンドの基本的な使い方を確認する</li>
            <li><code>man 1 chmod</code> - 権限指定の詳細を確認する</li>
            <li><code>man 7 hier</code> - Linux の標準的なディレクトリ構成を確認する</li>
            <li><code>man 1 bash</code> - シェルの基本挙動を確認する</li>
        </ul>

        <h3>主要ディストリビューションの公式ドキュメント</h3>
        <ul>
            <li><a href="https://help.ubuntu.com/" target="_blank" rel="noopener noreferrer">Ubuntu Documentation</a></li>
            <li><a href="https://docs.redhat.com/" target="_blank" rel="noopener noreferrer">Red Hat Documentation</a></li>
            <li><a href="https://www.debian.org/doc/" target="_blank" rel="noopener noreferrer">Debian Documentation</a></li>
        </ul>

        <h3>学習を続けるときの見方</h3>
        <ul>
            <li>まず本書の該当章で全体像をつかみ、次に <code>man</code> でコマンド単位の詳細を確認する</li>
            <li>ディストリ差分が出てきたら、使っているディストリビューションの公式ドキュメントを優先する</li>
            <li>本番環境で試す前に、手元の検証環境や仮想マシンで再現してから実行する</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>目次へ：</strong><a href="../">目次</a>に戻り、必要な章を参照してください。
    </div>
</div>
