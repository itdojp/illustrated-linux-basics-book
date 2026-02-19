---
layout: chapter
title: "第2章：ファイル権限とユーザー管理"
chapter: 2
---

<div class="section">
    <h1>第2章：ファイル権限とユーザー管理</h1>
    
    <h2>2.0 この章で学ぶこと</h2>
    
    <div class="explanation">
        <ul>
            <li><code>ls -l</code> の出力から、権限（r/w/x）と所有者/グループを読み取れる</li>
            <li><code>chmod</code>/<code>chown</code>/<code>chgrp</code> で権限と所有者を変更できる</li>
            <li>ユーザー/グループ管理の基本コマンドを把握できる</li>
        </ul>
    </div>
    
    <h2>2.1 ファイル権限の仕組み</h2>
    
    <div class="diagram-container">
        <svg width="850" height="500" viewBox="0 0 850 500">
            <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">Linuxの権限システム</text>
            
            <!-- ls -l の出力例 -->
            <rect x="50" y="60" width="750" height="80" fill="#f5f5f5" stroke="#333" stroke-width="2" rx="5"/>
            <text x="70" y="90" font-family="monospace" font-size="16" fill="#333">-rwxr-xr--  1  user  group  1024  Jan 15 10:30  script.sh</text>
            
            <!-- 各部分の説明 -->
            <!-- ファイルタイプ -->
            <line x1="70" y1="100" x2="70" y2="160" stroke="#e74c3c" stroke-width="2"/>
            <rect x="20" y="160" width="100" height="60" fill="#e74c3c" rx="5"/>
            <text x="70" y="185" text-anchor="middle" fill="white" font-size="12" font-weight="bold">ファイルタイプ</text>
            <text x="70" y="205" text-anchor="middle" fill="white" font-size="10">- = ファイル</text>
            <text x="70" y="215" text-anchor="middle" fill="white" font-size="10">d = ディレクトリ</text>
            
            <!-- 所有者権限 -->
            <line x1="110" y1="100" x2="110" y2="160" stroke="#3498db" stroke-width="2"/>
            <rect x="130" y="160" width="120" height="80" fill="#3498db" rx="5"/>
            <text x="190" y="185" text-anchor="middle" fill="white" font-size="12" font-weight="bold">所有者権限</text>
            <text x="190" y="205" text-anchor="middle" fill="white" font-size="10">r = 読み取り(4)</text>
            <text x="190" y="215" text-anchor="middle" fill="white" font-size="10">w = 書き込み(2)</text>
            <text x="190" y="225" text-anchor="middle" fill="white" font-size="10">x = 実行(1)</text>
            
            <!-- グループ権限 -->
            <line x1="155" y1="100" x2="190" y2="160" stroke="#2ecc71" stroke-width="2"/>
            <rect x="260" y="160" width="120" height="80" fill="#2ecc71" rx="5"/>
            <text x="320" y="185" text-anchor="middle" fill="white" font-size="12" font-weight="bold">グループ権限</text>
            <text x="320" y="205" text-anchor="middle" fill="white" font-size="10">r = 読み取り(4)</text>
            <text x="320" y="215" text-anchor="middle" fill="white" font-size="10">- = なし(0)</text>
            <text x="320" y="225" text-anchor="middle" fill="white" font-size="10">x = 実行(1)</text>
            
            <!-- その他権限 -->
            <line x1="200" y1="100" x2="270" y2="160" stroke="#f39c12" stroke-width="2"/>
            <rect x="390" y="160" width="120" height="80" fill="#f39c12" rx="5"/>
            <text x="450" y="185" text-anchor="middle" fill="white" font-size="12" font-weight="bold">その他権限</text>
            <text x="450" y="205" text-anchor="middle" fill="white" font-size="10">r = 読み取り(4)</text>
            <text x="450" y="215" text-anchor="middle" fill="white" font-size="10">- = なし(0)</text>
            <text x="450" y="225" text-anchor="middle" fill="white" font-size="10">- = なし(0)</text>
            
            <!-- 数値表記 -->
            <g transform="translate(550, 160)">
                <rect x="0" y="0" width="250" height="80" fill="#9b59b6" rx="5"/>
                <text x="125" y="25" text-anchor="middle" fill="white" font-size="14" font-weight="bold">数値表記</text>
                <text x="125" y="45" text-anchor="middle" fill="white" font-size="12">rwx r-x r-- = 754</text>
                <text x="125" y="60" text-anchor="middle" fill="white" font-size="10">7(4+2+1) 5(4+0+1) 4(4+0+0)</text>
            </g>
            
            <!-- よく使う権限パターン -->
            <g transform="translate(50, 280)">
                <rect x="0" y="0" width="750" height="180" fill="#ecf0f1" rx="10"/>
                <text x="20" y="30" font-size="16" font-weight="bold" fill="#2c3e50">よく使う権限パターン</text>
                
                <text x="20" y="60" font-family="monospace" font-size="14" fill="#333">755 (rwxr-xr-x)</text>
                <text x="200" y="60" font-size="12" fill="#555">→ 実行ファイル、スクリプト（所有者は全権限、他は読み実行のみ）</text>
                
                <text x="20" y="90" font-family="monospace" font-size="14" fill="#333">644 (rw-r--r--)</text>
                <text x="200" y="90" font-size="12" fill="#555">→ 通常のファイル（所有者は読み書き、他は読み取りのみ）</text>
                
                <text x="20" y="120" font-family="monospace" font-size="14" fill="#333">600 (rw-------)</text>
                <text x="200" y="120" font-size="12" fill="#555">→ 秘密鍵など（所有者のみアクセス可能）</text>
                
                <text x="20" y="150" font-family="monospace" font-size="14" fill="#333">777 (rwxrwxrwx)</text>
                <text x="200" y="150" font-size="12" fill="#e74c3c">→ ⚠️ 危険！全員が全権限（避けるべき）</text>
            </g>
        </svg>
    </div>

    <div class="key-point">
        <strong>補足：</strong>ディレクトリの <code>x</code> は「実行」ではなく「入れる/探索できる（パスをたどれる）」権限です。<code>r</code> は一覧表示、<code>w</code> は作成/削除/名前変更に関係します。
    </div>
    
    <h2>2.2 権限の変更コマンド</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>chmod - 権限変更</h3>
            <div class="command-box">
$ chmod 755 script.sh<br>
$ chmod u+x file.txt<br>
$ chmod go-w important.txt
            </div>
            <p><strong>数値指定：</strong></p>
            <ul>
                <li>4 = 読み取り (r)</li>
                <li>2 = 書き込み (w)</li>
                <li>1 = 実行 (x)</li>
            </ul>
            <p><strong>記号指定：</strong></p>
            <ul>
                <li>u = 所有者 (user)</li>
                <li>g = グループ (group)</li>
                <li>o = その他 (others)</li>
                <li>a = 全員 (all)</li>
            </ul>
        </div>
        
        <div class="command-card">
            <h3>chown - 所有者変更</h3>
            <div class="command-box">
$ sudo chown user file.txt<br>
$ sudo chown user:group file.txt<br>
$ sudo chown -R user:group directory/
            </div>
            <p>オプション：</p>
            <ul>
                <li><code>-R</code> ディレクトリ内を再帰的に変更</li>
            </ul>
        </div>
        
        <div class="command-card">
            <h3>chgrp - グループ変更</h3>
            <div class="command-box">
$ sudo chgrp developers project/<br>
$ sudo chgrp -R www-data /var/www/
            </div>
            <p>グループのみを変更したいときに使用します。</p>
        </div>
    </div>
    
    <h2>2.3 ユーザーとグループ管理</h2>
    
    <div class="diagram-container">
        <svg width="800" height="400" viewBox="0 0 800 400">
            <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ユーザーとグループの関係</text>
            
            <!-- ユーザー -->
            <g transform="translate(100, 60)">
                <circle cx="50" cy="50" r="40" fill="#3498db"/>
                <text x="50" y="55" text-anchor="middle" fill="white" font-size="14" font-weight="bold">alice</text>
                <text x="50" y="110" text-anchor="middle" font-size="12">ユーザー</text>
            </g>
            
            <g transform="translate(250, 60)">
                <circle cx="50" cy="50" r="40" fill="#3498db"/>
                <text x="50" y="55" text-anchor="middle" fill="white" font-size="14" font-weight="bold">bob</text>
                <text x="50" y="110" text-anchor="middle" font-size="12">ユーザー</text>
            </g>
            
            <g transform="translate(400, 60)">
                <circle cx="50" cy="50" r="40" fill="#3498db"/>
                <text x="50" y="55" text-anchor="middle" fill="white" font-size="14" font-weight="bold">carol</text>
                <text x="50" y="110" text-anchor="middle" font-size="12">ユーザー</text>
            </g>
            
            <!-- グループ -->
            <g transform="translate(100, 200)">
                <rect x="0" y="0" width="200" height="80" fill="#2ecc71" rx="10" opacity="0.7"/>
                <text x="100" y="40" text-anchor="middle" fill="white" font-size="16" font-weight="bold">developers</text>
                <text x="100" y="60" text-anchor="middle" fill="white" font-size="12">グループ</text>
            </g>
            
            <g transform="translate(350, 200)">
                <rect x="0" y="0" width="200" height="80" fill="#e74c3c" rx="10" opacity="0.7"/>
                <text x="100" y="40" text-anchor="middle" fill="white" font-size="16" font-weight="bold">admin</text>
                <text x="100" y="60" text-anchor="middle" fill="white" font-size="12">グループ</text>
            </g>
            
            <!-- 矢印（所属関係） -->
            <line x1="150" y1="140" x2="180" y2="200" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
            <line x1="300" y1="140" x2="250" y2="200" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
            <line x1="300" y1="140" x2="400" y2="200" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
            <line x1="450" y1="140" x2="480" y2="200" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
            
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
                </marker>
            </defs>
            
            <!-- 説明 -->
            <text x="400" y="320" text-anchor="middle" font-size="14" fill="#555">1人のユーザーは複数のグループに所属できる</text>
            <text x="400" y="345" text-anchor="middle" font-size="14" fill="#555">ファイルやディレクトリはユーザーとグループで管理される</text>
        </svg>
    </div>

    <div class="key-point">
        <strong>補足：</strong>管理者権限（<code>sudo</code>）を使えるユーザーは、ディストリビューションにより <code>sudo</code> グループ（Debian/Ubuntu系）や <code>wheel</code> グループ（RHEL系）に所属することが多いです。
    </div>
    
    <h2>2.4 ユーザー管理コマンド</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>useradd - ユーザー追加</h3>
            <div class="command-box">
$ sudo useradd newuser<br>
$ sudo useradd -m -s /bin/bash john<br>
$ sudo useradd -G developers alice
            </div>
            <p>オプション：</p>
            <ul>
                <li><code>-m</code> ホームディレクトリ作成</li>
                <li><code>-s</code> デフォルトシェル指定</li>
                <li><code>-G</code> 追加グループ指定</li>
            </ul>
        </div>
        
        <div class="command-card">
            <h3>passwd - パスワード設定</h3>
            <div class="command-box">
$ sudo passwd newuser<br>
$ passwd  # 自分のパスワード変更
            </div>
            <p>強力なパスワードを設定しよう</p>
        </div>
        
        <div class="command-card">
            <h3>usermod - ユーザー情報変更</h3>
            <div class="command-box">
$ sudo usermod -aG sudo alice<br>
$ sudo usermod -s /bin/zsh bob<br>
$ sudo usermod -L baduser  # ロック
            </div>
            <p><code>-aG</code> グループに追加（-a なしだと置換）</p>
        </div>
        
        <div class="command-card">
            <h3>userdel - ユーザー削除</h3>
            <div class="command-box">
$ sudo userdel olduser<br>
$ sudo userdel -r olduser  # ホームも削除
            </div>
            <p>⚠️ <code>-r</code> はホームディレクトリも削除します。</p>
        </div>
        
        <div class="command-card">
            <h3>groupadd - グループ追加</h3>
            <div class="command-box">
$ sudo groupadd developers<br>
$ sudo groupadd -g 1500 special
            </div>
            <p><code>-g</code> グループIDを指定します。</p>
        </div>
        
        <div class="command-card">
            <h3>groups - 所属グループ確認</h3>
            <div class="command-box">
$ groups<br>
$ groups alice<br>
$ id alice  # より詳細な情報
            </div>
            <p>ユーザーの所属グループを確認します。</p>
        </div>
    </div>
    
    <h2>2.5 特殊な権限</h2>
    
    <div class="explanation">
        <h3>SUID (Set User ID)</h3>
        <div class="command-box">$ chmod u+s program</div>
        <p>実行時に所有者の権限で動作します（例：passwd コマンド）。</p>
        
        <h3>SGID (Set Group ID)</h3>
        <div class="command-box">$ chmod g+s directory/</div>
        <p>ディレクトリ内の新規ファイルは同じグループになります。</p>
        
        <h3>スティッキービット</h3>
        <div class="command-box">$ chmod +t /tmp</div>
        <p>共有ディレクトリで、他人のファイルを削除できないようにする（削除できるのはファイル所有者/ディレクトリ所有者/root など）。</p>
    </div>
    
    <div class="important-note">
        <h3>⚠️ セキュリティの基本原則</h3>
        <ul>
            <li><strong>最小権限の原則</strong>：必要最小限の権限のみを付与</li>
            <li><strong>777は避ける</strong>：全員に全権限は危険</li>
            <li><strong>sudoの適切な使用</strong>：管理者権限は必要なときだけ</li>
            <li><strong>定期的な確認</strong>：不要なユーザーや権限を定期的に見直す</li>
        </ul>
    </div>
    
    <h2>2.6 まとめ</h2>
    
    <div class="explanation">
        <ul>
            <li>権限は「所有者/グループ/その他」に対して r/w/x を設定する</li>
            <li><code>chmod</code> は数値指定と記号指定の両方がある</li>
            <li>安易な <code>777</code> は避け、必要最小限の権限にする</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>次章予告：</strong>次章では、テキスト編集（<code>vi</code>）とテキスト処理、パッケージ管理の基本をまとめて扱います。
    </div>
</div>
