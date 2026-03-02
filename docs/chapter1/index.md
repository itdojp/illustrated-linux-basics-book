---
layout: chapter
title: "第1章：必須コマンド15選"
chapter: 1
---

<div class="section">
    <h1>第1章：必須コマンド15選</h1>
    
    <h2>1.0 この章で学ぶこと</h2>
    
    <div class="explanation">
        <ul>
            <li>Linuxで頻出するコマンドを俯瞰できる</li>
            <li>ファイル操作や検索など、基本用途を押さえたうえで実行例を試せる</li>
            <li>パイプ（<code>|</code>）とリダイレクト（<code>&gt;</code>/<code>&gt;&gt;</code>）でコマンドを組み合わせられる</li>
        </ul>
    </div>
    
    <div class="key-point">
        <strong>読み方：</strong>本章はコマンドの全体像を整理する章です。権限は <a href="../chapter2/">第2章</a>、テキスト処理・パッケージ管理は <a href="../chapter3/">第3章</a> で扱います。
    </div>
    
    <h2>1.1 まず押さえる必須コマンド</h2>
    
    <div class="diagram-container">
        <svg width="850" height="700" viewBox="0 0 850 700">
            <!-- Title -->
            <text x="425" y="30" text-anchor="middle" font-size="24" font-weight="bold" fill="#2c3e50">Linux 必須コマンド15選</text>
            
            <!-- ファイル操作系 (最重要) -->
            <g transform="translate(50, 60)">
                <rect x="0" y="0" width="750" height="120" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" rx="10"/>
                <text x="20" y="30" font-size="18" font-weight="bold" fill="#2e7d32">ファイル操作（最重要）</text>
                
                <!-- ls -->
                <rect x="20" y="50" width="100" height="50" fill="#4caf50" rx="5"/>
                <text x="70" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ls</text>
                <text x="70" y="95" text-anchor="middle" fill="white" font-size="10">一覧表示</text>
                
                <!-- cd -->
                <rect x="130" y="50" width="100" height="50" fill="#66bb6a" rx="5"/>
                <text x="180" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">cd</text>
                <text x="180" y="95" text-anchor="middle" fill="white" font-size="10">移動</text>
                
                <!-- pwd -->
                <rect x="240" y="50" width="100" height="50" fill="#81c784" rx="5"/>
                <text x="290" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">pwd</text>
                <text x="290" y="95" text-anchor="middle" fill="white" font-size="10">現在地</text>
                
                <!-- mkdir -->
                <rect x="350" y="50" width="100" height="50" fill="#4caf50" rx="5"/>
                <text x="400" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">mkdir</text>
                <text x="400" y="95" text-anchor="middle" fill="white" font-size="10">作成</text>
                
                <!-- rm -->
                <rect x="460" y="50" width="100" height="50" fill="#66bb6a" rx="5"/>
                <text x="510" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">rm</text>
                <text x="510" y="95" text-anchor="middle" fill="white" font-size="10">削除</text>
                
                <!-- cp/mv -->
                <rect x="570" y="50" width="150" height="50" fill="#81c784" rx="5"/>
                <text x="645" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">cp / mv</text>
                <text x="645" y="95" text-anchor="middle" fill="white" font-size="10">コピー/移動</text>
            </g>
            
            <!-- 権限管理系 -->
            <g transform="translate(50, 200)">
                <rect x="0" y="0" width="750" height="120" fill="#fff3e0" stroke="#ff9800" stroke-width="2" rx="10"/>
                <text x="20" y="30" font-size="18" font-weight="bold" fill="#e65100">権限・ユーザー管理</text>
                
                <!-- chmod -->
                <rect x="20" y="50" width="120" height="50" fill="#ff9800" rx="5"/>
                <text x="80" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">chmod</text>
                <text x="80" y="95" text-anchor="middle" fill="white" font-size="10">権限変更</text>
                
                <!-- chown -->
                <rect x="150" y="50" width="120" height="50" fill="#ffa726" rx="5"/>
                <text x="210" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">chown</text>
                <text x="210" y="95" text-anchor="middle" fill="white" font-size="10">所有者変更</text>
                
                <!-- sudo -->
                <rect x="280" y="50" width="120" height="50" fill="#ffb74d" rx="5"/>
                <text x="340" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">sudo</text>
                <text x="340" y="95" text-anchor="middle" fill="white" font-size="10">管理者権限</text>
            </g>
            
            <!-- テキスト処理系 -->
            <g transform="translate(50, 340)">
                <rect x="0" y="0" width="750" height="120" fill="#e3f2fd" stroke="#2196f3" stroke-width="2" rx="10"/>
                <text x="20" y="30" font-size="18" font-weight="bold" fill="#0d47a1">テキスト処理</text>
                
                <!-- cat -->
                <rect x="20" y="50" width="100" height="50" fill="#2196f3" rx="5"/>
                <text x="70" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">cat</text>
                <text x="70" y="95" text-anchor="middle" fill="white" font-size="10">表示</text>
                
                <!-- grep -->
                <rect x="130" y="50" width="100" height="50" fill="#42a5f5" rx="5"/>
                <text x="180" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">grep</text>
                <text x="180" y="95" text-anchor="middle" fill="white" font-size="10">検索</text>
                
                <!-- echo -->
                <rect x="240" y="50" width="100" height="50" fill="#64b5f6" rx="5"/>
                <text x="290" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">echo</text>
                <text x="290" y="95" text-anchor="middle" fill="white" font-size="10">出力</text>
            </g>
            
            <!-- システム管理系 -->
            <g transform="translate(50, 480)">
                <rect x="0" y="0" width="750" height="120" fill="#fce4ec" stroke="#e91e63" stroke-width="2" rx="10"/>
                <text x="20" y="30" font-size="18" font-weight="bold" fill="#880e4f">システム管理</text>
                
                <!-- ps -->
                <rect x="20" y="50" width="100" height="50" fill="#e91e63" rx="5"/>
                <text x="70" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ps</text>
                <text x="70" y="95" text-anchor="middle" fill="white" font-size="10">プロセス</text>
                
                <!-- kill -->
                <rect x="130" y="50" width="100" height="50" fill="#ec407a" rx="5"/>
                <text x="180" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">kill</text>
                <text x="180" y="95" text-anchor="middle" fill="white" font-size="10">終了</text>
                
                <!-- man -->
                <rect x="240" y="50" width="100" height="50" fill="#f06292" rx="5"/>
                <text x="290" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">man</text>
                <text x="290" y="95" text-anchor="middle" fill="white" font-size="10">ヘルプ</text>
            </g>
            
            <!-- 重要度インジケーター -->
            <g transform="translate(50, 620)">
                <text x="0" y="20" font-size="14" font-weight="bold" fill="#2c3e50">重要度：</text>
                <rect x="80" y="5" width="20" height="20" fill="#4caf50"/>
                <text x="105" y="20" font-size="12" fill="#2c3e50">最重要（毎日使う）</text>
                <rect x="230" y="5" width="20" height="20" fill="#ff9800"/>
                <text x="255" y="20" font-size="12" fill="#2c3e50">重要（頻繁に使う）</text>
                <rect x="380" y="5" width="20" height="20" fill="#2196f3"/>
                <text x="405" y="20" font-size="12" fill="#2c3e50">便利（知っておくと良い）</text>
            </g>
        </svg>
    </div>
    
    <h2>1.2 各コマンドの詳細</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>1. ls - ファイル一覧表示</h3>
            <div class="command-box">$ ls -lah</div>
            <div class="output-box">
drwxr-xr-x  5 user user 4.0K Jan 15 10:30 .<br>
drwxr-xr-x  3 user user 4.0K Jan 10 09:15 ..<br>
-rw-r--r--  1 user user  220 Jan 12 14:22 file.txt
            </div>
            <p>オプション: <code>-l</code> 詳細表示、<code>-a</code> 隠しファイルも表示、<code>-h</code> サイズを読みやすく</p>
        </div>
        
        <div class="command-card">
            <h3>2. cd - ディレクトリ移動</h3>
            <div class="command-box">$ cd /home/user/Documents</div>
            <p>特殊な使い方：</p>
            <ul>
                <li><code>cd ~</code> ホームディレクトリへ</li>
                <li><code>cd ..</code> 親ディレクトリへ</li>
                <li><code>cd -</code> 直前のディレクトリへ</li>
            </ul>
        </div>
        
        <div class="command-card">
            <h3>3. pwd - 現在地表示</h3>
            <div class="command-box">$ pwd</div>
            <div class="output-box">/home/user/Documents</div>
            <p>現在の作業ディレクトリが不明な場合は、このコマンドで確認します。</p>
        </div>
        
        <div class="command-card">
            <h3>4. mkdir - ディレクトリ作成</h3>
            <div class="command-box">$ mkdir new_folder<br>$ mkdir -p parent/child</div>
            <p><code>-p</code> 親ディレクトリも同時作成</p>
        </div>
        
        <div class="command-card">
            <h3>5. rm - ファイル削除</h3>
            <div class="command-box">$ rm file.txt<br>$ rm -rf directory</div>
            <p><strong>注意：</strong><code>-rf</code> は強制削除であり、元に戻せません。練習ではテスト用ディレクトリ内で試し、<code>/</code> やホームディレクトリ直下など重要な場所では実行しないでください。</p>
        </div>
        
        <div class="command-card">
            <h3>6. cp / mv - コピー/移動</h3>
            <div class="command-box">$ cp source.txt dest.txt<br>$ cp -r source_dir dest_dir<br>$ mv old.txt new.txt<br>$ mv file.txt ~/</div>
            <p>コピー（cp）と移動/名前変更（mv）に使用</p>
        </div>
        
        <div class="command-card">
            <h3>7. chmod - 権限変更</h3>
            <div class="command-box">$ chmod 755 script.sh<br>$ chmod +x script.sh</div>
            <p>755 = 所有者:全権限、他:読み実行のみ</p>
        </div>
        
        <div class="command-card">
            <h3>8. chown - 所有者変更</h3>
            <div class="command-box">$ sudo chown user:group file.txt</div>
            <p>ファイルの所有者とグループを変更</p>
        </div>
        
        <div class="command-card">
            <h3>9. sudo - 管理者権限で実行</h3>
            <div class="command-box">$ sudo apt update<br>$ sudo systemctl restart apache2</div>
            <p>システム変更時に必要</p>
        </div>
        
        <div class="command-card">
            <h3>10. cat - ファイル内容表示</h3>
            <div class="command-box">$ cat file.txt<br>$ cat file1.txt file2.txt > merged.txt</div>
            <p>ファイルの結合にも使用可能</p>
        </div>
        
        <div class="command-card">
            <h3>11. grep - 文字列検索</h3>
            <div class="command-box">$ grep "error" log.txt<br>$ ps aux | grep apache</div>
            <p>パイプと組み合わせて強力に</p>
        </div>
        
        <div class="command-card">
            <h3>12. echo - 文字列出力</h3>
            <div class="command-box">$ echo "Hello World"<br>$ echo $PATH</div>
            <p>変数の確認にも便利</p>
        </div>
        
        <div class="command-card">
            <h3>13. ps - プロセス表示</h3>
            <div class="command-box">$ ps aux<br>$ ps -ef</div>
            <p>実行中のプログラムを確認（<code>aux</code>はBSD形式、<code>-ef</code>はSystem V形式）</p>
        </div>

        <div class="command-card">
            <h3>14. kill - プロセス終了</h3>
            <div class="command-box">$ kill 1234<br>$ kill -TERM 1234<br>$ kill -KILL 1234</div>
            <p>基本は TERM（穏やかに終了）です。KILL（-9）は最終手段です。</p>
        </div>

        <div class="command-card">
            <h3>15. man - マニュアル表示</h3>
            <div class="command-box">$ man ls<br>$ man chmod</div>
            <p>不明点はマニュアルで確認します（終了は <code>q</code>）。</p>
        </div>
    </div>
    
    <h2>1.3 コマンドの組み合わせ技</h2>
    
    <div class="explanation">
        <h3>パイプ（|）を使った連携</h3>
        <div class="command-box">$ ls -la | grep ".txt"</div>
        <p>→ テキストファイルだけを表示</p>
        
        <div class="command-box">$ ps aux | grep python | grep -v grep</div>
        <p>→ Python関連のプロセスを表示（grep自身は除外）</p>

        <div class="key-point">
            <strong>補足：</strong><code>ps | grep</code> 以外に、<code>pgrep</code> でプロセス名から検索する方法もあります。
            <div class="command-box">$ pgrep -a python</div>
            <p>（<code>-a</code> は PID とコマンドライン全体を表示）</p>
        </div>
        
        <h3>リダイレクト（>）で結果を保存</h3>
        <div class="command-box">$ ls -la > file_list.txt</div>
        <p>→ ファイル一覧をテキストファイルに保存</p>
        
        <div class="command-box">$ echo "新しい行" >> existing.txt</div>
        <p>→ 既存ファイルに追記（>>は追記、>は上書き）</p>
    </div>
    
    <h2>1.4 まとめ</h2>
    
    <div class="explanation">
        <ul>
            <li>まずは <code>ls</code>/<code>cd</code>/<code>pwd</code> で現在位置と内容を確認する</li>
            <li><code>grep</code> やパイプで必要な情報だけを抽出できる</li>
            <li>権限やユーザーの話が出てきたら <a href="../chapter2/">第2章</a> を参照する</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>次章予告：</strong>次章では、Linux の権限（r/w/x）とユーザー／グループ管理の基本を整理します。
    </div>
</div>
