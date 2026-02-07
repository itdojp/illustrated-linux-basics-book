---
layout: chapter
title: "第3章：テキスト処理とパッケージ管理"  
chapter: 3
---

<div class="section">
    <h1>第3章：テキスト処理とパッケージ管理</h1>
    
    <h2>3.0 この章で学ぶこと</h2>
    
    <div class="explanation">
        <ul>
            <li><code>vi</code> の基本操作（編集・保存・終了）を把握できる</li>
            <li>テキスト処理コマンドで「必要な行だけを抜き出す」流れを作れる</li>
            <li>パッケージ管理（APT/YUM(DNF)）でインストール・更新・削除ができる</li>
        </ul>
    </div>
    
    <h2>3.1 viエディタの基本操作</h2>
    
    <div class="diagram-container">
        <svg width="800" height="450" viewBox="0 0 800 450">
            <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">viエディタのモード遷移</text>
            
            <!-- ノーマルモード -->
            <circle cx="400" cy="150" r="80" fill="#3498db"/>
            <text x="400" y="145" text-anchor="middle" fill="white" font-size="16" font-weight="bold">ノーマル</text>
            <text x="400" y="165" text-anchor="middle" fill="white" font-size="14">モード</text>
            <text x="400" y="185" text-anchor="middle" fill="white" font-size="12">(移動・削除)</text>
            
            <!-- 挿入モード -->
            <circle cx="200" cy="300" r="70" fill="#2ecc71"/>
            <text x="200" y="295" text-anchor="middle" fill="white" font-size="16" font-weight="bold">挿入</text>
            <text x="200" y="315" text-anchor="middle" fill="white" font-size="14">モード</text>
            <text x="200" y="335" text-anchor="middle" fill="white" font-size="12">(文字入力)</text>
            
            <!-- コマンドモード -->
            <circle cx="600" cy="300" r="70" fill="#e74c3c"/>
            <text x="600" y="295" text-anchor="middle" fill="white" font-size="16" font-weight="bold">コマンド</text>
            <text x="600" y="315" text-anchor="middle" fill="white" font-size="14">モード</text>
            <text x="600" y="335" text-anchor="middle" fill="white" font-size="12">(保存・終了)</text>
            
            <!-- 矢印と説明 -->
            <!-- ノーマル → 挿入 -->
            <path d="M 340 180 Q 270 240 230 260" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
            <text x="285" y="210" font-size="14" fill="#333" font-weight="bold">i, a, o</text>
            
            <!-- 挿入 → ノーマル -->
            <path d="M 230 240 Q 270 180 340 150" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
            <text x="285" y="170" font-size="14" fill="#333" font-weight="bold">ESC</text>
            
            <!-- ノーマル → コマンド -->
            <path d="M 460 180 Q 530 240 570 260" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
            <text x="515" y="210" font-size="14" fill="#333" font-weight="bold">:</text>
            
            <!-- コマンド → ノーマル -->
            <path d="M 570 240 Q 530 180 460 150" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
            <text x="515" y="170" font-size="14" fill="#333" font-weight="bold">ESC</text>
            
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
                </marker>
            </defs>
            
            <!-- 基本操作一覧 -->
            <g transform="translate(50, 380)">
                <rect x="0" y="0" width="700" height="50" fill="#f5f5f5" stroke="#333" rx="5"/>
                <text x="10" y="25" font-size="12" font-weight="bold" fill="#333">最低限覚える操作：</text>
                <text x="150" y="25" font-family="monospace" font-size="12" fill="#333">i (挿入) → ESC → :wq (保存して終了) または :q! (保存せず終了)</text>
            </g>
        </svg>
    </div>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>vi基本操作早見表</h3>
            <table class="comparison-table">
                <tr>
                    <th>操作</th>
                    <th>コマンド</th>
                    <th>説明</th>
                </tr>
                <tr>
                    <td>ファイルを開く</td>
                    <td><code>vi file.txt</code></td>
                    <td>viエディタでファイルを開く</td>
                </tr>
                <tr>
                    <td>挿入モードへ</td>
                    <td><code>i</code></td>
                    <td>カーソル位置から入力開始</td>
                </tr>
                <tr>
                    <td>行末に追加</td>
                    <td><code>a</code></td>
                    <td>カーソルの後から入力</td>
                </tr>
                <tr>
                    <td>新しい行</td>
                    <td><code>o</code></td>
                    <td>下に新しい行を作成</td>
                </tr>
                <tr>
                    <td>ノーマルモードへ</td>
                    <td><code>ESC</code></td>
                    <td>編集を終了</td>
                </tr>
                <tr>
                    <td>保存して終了</td>
                    <td><code>:wq</code></td>
                    <td>変更を保存して終了</td>
                </tr>
                <tr>
                    <td>保存せず終了</td>
                    <td><code>:q!</code></td>
                    <td>変更を破棄して終了</td>
                </tr>
                <tr>
                    <td>1行削除</td>
                    <td><code>dd</code></td>
                    <td>カーソル行を削除</td>
                </tr>
                <tr>
                    <td>元に戻す</td>
                    <td><code>u</code></td>
                    <td>直前の操作を取り消し</td>
                </tr>
            </table>
        </div>
    </div>
    
    <h2>3.2 テキスト処理コマンド</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>cat - ファイル表示</h3>
            <div class="command-box">
$ cat file.txt<br>
$ cat -n file.txt  # 行番号付き<br>
$ cat file1.txt file2.txt > merged.txt
            </div>
            <p>複数ファイルの結合にも使用します。</p>
        </div>
        
        <div class="command-card">
            <h3>less / more - ページング表示</h3>
            <div class="command-box">
$ less large_file.txt<br>
$ cat file.txt | less
            </div>
            <p>操作：<code>Space</code>(次ページ) <code>b</code>(前ページ) <code>q</code>(終了)</p>
        </div>
        
        <div class="command-card">
            <h3>head / tail - 先頭/末尾表示</h3>
            <div class="command-box">
$ head -n 10 file.txt  # 先頭10行<br>
$ tail -n 20 file.txt  # 末尾20行<br>
$ tail -f /var/log/syslog  # リアルタイム監視
            </div>
            <p><code>-f</code> はログ監視に便利です。</p>
        </div>
        
        <div class="command-card">
            <h3>grep - パターン検索</h3>
            <div class="command-box">
$ grep "error" log.txt<br>
$ grep -i "Error" log.txt  # 大文字小文字無視<br>
$ grep -r "TODO" ./src/  # 再帰検索<br>
$ grep -v "debug" log.txt  # 除外
            </div>
            <p>正規表現も使用できます。</p>
        </div>
        
        <div class="command-card">
            <h3>sed - ストリームエディタ</h3>
            <div class="command-box">
$ sed 's/old/new/g' file.txt  # 置換<br>
$ sed -i 's/old/new/g' file.txt  # 直接編集<br>
$ sed '5d' file.txt  # 5行目削除
            </div>
            <p>一括置換に便利です。</p>
        </div>
        
        <div class="command-card">
            <h3>awk - テキスト処理言語</h3>
            <div class="command-box">
$ awk '{print $1}' file.txt  # 1列目表示<br>
$ awk -F: '{print $1}' /etc/passwd  # 区切り文字指定<br>
$ ps aux | awk '{print $2, $11}'  # PIDとコマンド
            </div>
            <p>列単位の処理に強力です。</p>
        </div>
    </div>
    
    <h2>3.3 パッケージ管理システム</h2>
    
    <div class="diagram-container">
        <svg width="850" height="400" viewBox="0 0 850 400">
            <text x="425" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">主要なパッケージ管理システム</text>
            
            <!-- Debian/Ubuntu系 -->
            <g transform="translate(50, 60)">
                <rect x="0" y="0" width="350" height="280" fill="#e8f4fd" stroke="#2196f3" stroke-width="2" rx="10"/>
                <text x="175" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#1976d2">Debian/Ubuntu系</text>
                
                <!-- APT -->
                <rect x="20" y="50" width="310" height="100" fill="#2196f3" rx="5"/>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="16" font-weight="bold">APT (Advanced Package Tool)</text>
                <text x="175" y="100" text-anchor="middle" fill="white" font-size="12">高レベルパッケージ管理</text>
                <text x="175" y="120" text-anchor="middle" fill="white" font-family="monospace" font-size="11">apt update, apt install, apt remove</text>
                <text x="175" y="140" text-anchor="middle" fill="white" font-size="10">依存関係を自動解決</text>
                
                <!-- dpkg -->
                <rect x="20" y="170" width="310" height="80" fill="#64b5f6" rx="5"/>
                <text x="175" y="195" text-anchor="middle" fill="white" font-size="16" font-weight="bold">dpkg</text>
                <text x="175" y="215" text-anchor="middle" fill="white" font-size="12">低レベルパッケージ管理</text>
                <text x="175" y="235" text-anchor="middle" fill="white" font-family="monospace" font-size="11">dpkg -i package.deb</text>
                
                <!-- 例 -->
                <text x="20" y="275" font-size="12" fill="#333">例: Ubuntu, Debian, Linux Mint</text>
                <text x="20" y="295" font-size="12" fill="#333">ファイル形式: .deb</text>
            </g>
            
            <!-- RedHat/CentOS系 -->
            <g transform="translate(450, 60)">
                <rect x="0" y="0" width="350" height="280" fill="#ffebee" stroke="#f44336" stroke-width="2" rx="10"/>
                <text x="175" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#c62828">RedHat/CentOS系</text>
                
                <!-- YUM/DNF -->
                <rect x="20" y="50" width="310" height="100" fill="#f44336" rx="5"/>
                <text x="175" y="75" text-anchor="middle" fill="white" font-size="16" font-weight="bold">YUM / DNF</text>
                <text x="175" y="100" text-anchor="middle" fill="white" font-size="12">高レベルパッケージ管理</text>
                <text x="175" y="120" text-anchor="middle" fill="white" font-family="monospace" font-size="11">yum install, dnf update</text>
                <text x="175" y="140" text-anchor="middle" fill="white" font-size="10">依存関係を自動解決</text>
                
                <!-- RPM -->
                <rect x="20" y="170" width="310" height="80" fill="#ef5350" rx="5"/>
                <text x="175" y="195" text-anchor="middle" fill="white" font-size="16" font-weight="bold">RPM</text>
                <text x="175" y="215" text-anchor="middle" fill="white" font-size="12">低レベルパッケージ管理</text>
                <text x="175" y="235" text-anchor="middle" fill="white" font-family="monospace" font-size="11">rpm -ivh package.rpm</text>
                
                <!-- 例 -->
                <text x="20" y="275" font-size="12" fill="#333">例: RHEL, CentOS, Fedora, Rocky Linux</text>
                <text x="20" y="295" font-size="12" fill="#333">ファイル形式: .rpm</text>
            </g>
        </svg>
    </div>
    
    <h2>3.4 APT (Debian/Ubuntu)</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>パッケージリスト更新</h3>
            <div class="command-box">$ sudo apt update</div>
            <p>リポジトリから最新のパッケージ情報を取得</p>
        </div>
        
        <div class="command-card">
            <h3>パッケージインストール</h3>
            <div class="command-box">
$ sudo apt install nginx<br>
$ sudo apt install vim git curl -y
            </div>
            <p><code>-y</code> で確認をスキップします。</p>
        </div>
        
        <div class="command-card">
            <h3>パッケージ削除</h3>
            <div class="command-box">
$ sudo apt remove package-name<br>
$ sudo apt purge package-name  # 設定も削除<br>
$ sudo apt autoremove  # 不要な依存削除
            </div>
            <p><code>purge</code> は設定ファイルも削除します。</p>
        </div>
        
        <div class="command-card">
            <h3>システム更新</h3>
            <div class="command-box">
$ sudo apt update && sudo apt upgrade<br>
$ sudo apt full-upgrade  # カーネルも更新
            </div>
            <p>定期的な更新でセキュリティを保ちます。</p>
        </div>
        
        <div class="command-card">
            <h3>パッケージ検索</h3>
            <div class="command-box">
$ apt search keyword<br>
$ apt show package-name  # 詳細情報<br>
$ apt list --installed  # インストール済み一覧
            </div>
            <p>必要なパッケージを探します。</p>
        </div>
    </div>
    
    <h2>3.5 YUM/DNF (RedHat/CentOS)</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>パッケージインストール</h3>
            <div class="command-box">
$ sudo yum install httpd<br>
$ sudo dnf install postgresql  # Fedora/RHEL8+
            </div>
            <p>RHEL系（RHEL/CentOS互換）では、7系は yum、8+ は dnf を利用します。</p>
        </div>
        
        <div class="command-card">
            <h3>パッケージ削除</h3>
            <div class="command-box">
$ sudo yum remove package-name<br>
$ sudo yum autoremove
            </div>
            <p>依存関係も考慮して削除します。</p>
        </div>
        
        <div class="command-card">
            <h3>システム更新</h3>
            <div class="command-box">
$ sudo yum update<br>
$ sudo yum upgrade  # 古いパッケージも削除
            </div>
            <p>セキュリティアップデートを含みます。</p>
        </div>
    </div>
    
    <h2>3.6 パッケージ管理のベストプラクティス</h2>
    
    <div class="explanation">
        <h3>🔒 セキュリティ対策</h3>
        <ul>
            <li>定期的に <code>apt update && apt upgrade</code> を実行</li>
            <li>不要なパッケージは削除（攻撃対象を減らす）</li>
            <li>信頼できるリポジトリのみ使用</li>
        </ul>
        
        <h3>💡 トラブル回避のコツ</h3>
        <ul>
            <li>大規模更新前はバックアップを取る</li>
            <li>本番環境では事前にテスト環境で確認</li>
            <li><code>apt-mark hold package-name</code> で特定バージョン固定</li>
        </ul>
        
        <h3>🚀 便利な使い方</h3>
        <ul>
            <li><code>apt install -y</code> でスクリプト化しやすく</li>
            <li><code>which command</code> でコマンドの場所確認</li>
            <li><code>dpkg -L package</code> でインストールファイル一覧</li>
        </ul>
    </div>
    
    <h2>3.7 まとめ</h2>
    
    <div class="explanation">
        <ul>
            <li><code>vi</code> は「モード」の切り替えが基本（まずは編集→保存→終了を押さえる）</li>
            <li>テキスト処理は <code>grep</code> とパイプを起点にすると理解しやすい</li>
            <li>パッケージ管理は「更新（update）→インストール/アップグレード」の順を意識する</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>次章予告：</strong>次章では、よくあるエラーの読み方と対処のパターンを整理し、トラブルシューティングの基本を身につけます。
    </div>
</div>
