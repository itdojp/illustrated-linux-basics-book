---
layout: chapter
title: "第2章：基本操作マスター"
chapter: 2
---

<div class="section">
        <h1>第2章：基本操作マスター</h1>
        
        <h2>2.1 必須コマンド10選</h2>
        
        <div class="diagram-container">
            <svg width="850" height="600" viewBox="0 0 850 600">
                <!-- Central Linux Terminal -->
                <rect x="350" y="250" width="150" height="100" fill="#2c3e50" stroke="#34495e" stroke-width="3" rx="10"/>
                <text x="425" y="285" text-anchor="middle" fill="#27ae60" font-size="16" font-weight="bold">$ _</text>
                <text x="425" y="305" text-anchor="middle" fill="#27ae60" font-size="14">Linux Terminal</text>
                <text x="425" y="325" text-anchor="middle" fill="#ecf0f1" font-size="12">コマンドの中枢</text>
                
                <!-- Command boxes arranged around terminal -->
                <!-- ls -->
                <rect x="100" y="50" width="120" height="80" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="160" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ls</text>
                <text x="160" y="100" text-anchor="middle" fill="white" font-size="11">ファイル一覧</text>
                <text x="160" y="115" text-anchor="middle" fill="white" font-size="11">表示</text>
                <line x1="220" y1="90" x2="350" y2="250" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- cd -->
                <rect x="280" y="50" width="120" height="80" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="340" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">cd</text>
                <text x="340" y="100" text-anchor="middle" fill="white" font-size="11">ディレクトリ</text>
                <text x="340" y="115" text-anchor="middle" fill="white" font-size="11">移動</text>
                <line x1="340" y1="130" x2="410" y2="250" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- mkdir -->
                <rect x="460" y="50" width="120" height="80" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="520" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">mkdir</text>
                <text x="520" y="100" text-anchor="middle" fill="white" font-size="11">ディレクトリ</text>
                <text x="520" y="115" text-anchor="middle" fill="white" font-size="11">作成</text>
                <line x1="520" y1="130" x2="440" y2="250" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- rm -->
                <rect x="640" y="50" width="120" height="80" fill="#e67e22" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="700" y="80" text-anchor="middle" fill="white" font-size="14" font-weight="bold">rm</text>
                <text x="700" y="100" text-anchor="middle" fill="white" font-size="11">ファイル</text>
                <text x="700" y="115" text-anchor="middle" fill="white" font-size="11">削除</text>
                <line x1="640" y1="90" x2="500" y2="250" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- cp -->
                <rect x="100" y="200" width="120" height="80" fill="#9b59b6" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="160" y="230" text-anchor="middle" fill="white" font-size="14" font-weight="bold">cp</text>
                <text x="160" y="250" text-anchor="middle" fill="white" font-size="11">ファイル</text>
                <text x="160" y="265" text-anchor="middle" fill="white" font-size="11">コピー</text>
                <line x1="220" y1="240" x2="350" y2="280" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- mv -->
                <rect x="640" y="200" width="120" height="80" fill="#1abc9c" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="700" y="230" text-anchor="middle" fill="white" font-size="14" font-weight="bold">mv</text>
                <text x="700" y="250" text-anchor="middle" fill="white" font-size="11">ファイル</text>
                <text x="700" y="265" text-anchor="middle" fill="white" font-size="11">移動・名前変更</text>
                <line x1="640" y1="240" x2="500" y2="280" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- pwd -->
                <rect x="100" y="400" width="120" height="80" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="160" y="430" text-anchor="middle" fill="white" font-size="14" font-weight="bold">pwd</text>
                <text x="160" y="450" text-anchor="middle" fill="white" font-size="11">現在位置</text>
                <text x="160" y="465" text-anchor="middle" fill="white" font-size="11">表示</text>
                <line x1="220" y1="440" x2="350" y2="350" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- find -->
                <rect x="280" y="400" width="120" height="80" fill="#d35400" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="340" y="430" text-anchor="middle" fill="white" font-size="14" font-weight="bold">find</text>
                <text x="340" y="450" text-anchor="middle" fill="white" font-size="11">ファイル</text>
                <text x="340" y="465" text-anchor="middle" fill="white" font-size="11">検索</text>
                <line x1="340" y1="400" x2="410" y2="350" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- grep -->
                <rect x="460" y="400" width="120" height="80" fill="#8e44ad" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="520" y="430" text-anchor="middle" fill="white" font-size="14" font-weight="bold">grep</text>
                <text x="520" y="450" text-anchor="middle" fill="white" font-size="11">文字列</text>
                <text x="520" y="465" text-anchor="middle" fill="white" font-size="11">検索</text>
                <line x1="520" y1="400" x2="440" y2="350" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- ps -->
                <rect x="640" y="400" width="120" height="80" fill="#c0392b" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="700" y="430" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ps</text>
                <text x="700" y="450" text-anchor="middle" fill="white" font-size="11">プロセス</text>
                <text x="700" y="465" text-anchor="middle" fill="white" font-size="11">表示</text>
                <line x1="640" y1="440" x2="500" y2="350" stroke="#7f8c8d" stroke-width="2" opacity="0.6"/>
                
                <!-- Title -->
                <text x="425" y="30" text-anchor="middle" font-size="24" font-weight="bold" fill="#2c3e50">Linux 必須コマンド10選</text>
                
                <!-- Usage indicator -->
                <text x="50" y="570" font-size="12" fill="#7f8c8d">使用頻度: 高 ← → 低</text>
            </svg>
        </div>
        
        <div class="command-grid">
            <div class="command-card">
                <h3>ls - ファイル一覧</h3>
                <div class="command-box">$ ls -la</div>
                <div class="output-box">
drwxr-xr-x  5 user user 4096 Jan 15 10:30 .<br>
drwxr-xr-x  3 user user 4096 Jan 10 09:15 ..<br>
-rw-r--r--  1 user user  220 Jan 12 14:22 file.txt
                </div>
                <p><code>-l</code>: 詳細表示　<code>-a</code>: 隠しファイルも表示</p>
            </div>
            
            <div class="command-card">
                <h3>cd - ディレクトリ移動</h3>
                <div class="command-box">$ cd /home/user/Documents</div>
                <p>便利な使い方：</p>
                <ul>
                    <li><code>cd ~</code>: ホームディレクトリへ</li>
                    <li><code>cd ..</code>: 親ディレクトリへ</li>
                    <li><code>cd -</code>: 直前のディレクトリへ</li>
                </ul>
            </div>
            
            <div class="command-card">
                <h3>mkdir - ディレクトリ作成</h3>
                <div class="command-box">$ mkdir new_folder</div>
                <div class="command-box">$ mkdir -p parent/child/grandchild</div>
                <p><code>-p</code>: 親ディレクトリも同時に作成</p>
            </div>
            
            <div class="command-card">
                <h3>rm - ファイル削除</h3>
                <div class="command-box">$ rm file.txt</div>
                <div class="command-box">$ rm -rf directory</div>
                <p><code>-r</code>: ディレクトリも削除　<code>-f</code>: 強制削除</p>
                <p><strong>注意：</strong>削除したファイルは復元困難</p>
            </div>
        </div>
        
        <h2>2.2 パイプとリダイレクト</h2>
        
        <div class="diagram-container">
            <svg width="800" height="400" viewBox="0 0 800 400">
                <!-- Pipeline concept -->
                <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">パイプライン（|）の概念</text>
                
                <!-- Command 1 -->
                <rect x="50" y="80" width="120" height="60" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="110" y="100" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ls -la</text>
                <text x="110" y="120" text-anchor="middle" fill="white" font-size="12">ファイル一覧</text>
                
                <!-- Pipe symbol -->
                <rect x="200" y="100" width="40" height="20" fill="#e74c3c"/>
                <text x="220" y="115" text-anchor="middle" fill="white" font-size="16" font-weight="bold">|</text>
                
                <!-- Command 2 -->
                <rect x="270" y="80" width="120" height="60" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="330" y="100" text-anchor="middle" fill="white" font-size="14" font-weight="bold">grep "txt"</text>
                <text x="330" y="120" text-anchor="middle" fill="white" font-size="12">文字列検索</text>
                
                <!-- Pipe symbol -->
                <rect x="420" y="100" width="40" height="20" fill="#e74c3c"/>
                <text x="440" y="115" text-anchor="middle" fill="white" font-size="16" font-weight="bold">|</text>
                
                <!-- Command 3 -->
                <rect x="490" y="80" width="120" height="60" fill="#27ae60" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="550" y="100" text-anchor="middle" fill="white" font-size="14" font-weight="bold">sort</text>
                <text x="550" y="120" text-anchor="middle" fill="white" font-size="12">並び替え</text>
                
                <!-- Arrow -->
                <path d="M 650 110 L 700 110" stroke="#2c3e50" stroke-width="3" marker-end="url(#arrowhead)"/>
                <text x="725" y="115" font-size="14" fill="#2c3e50">結果出力</text>
                
                <!-- Data flow arrows -->
                <path d="M 170 110 L 200 110" stroke="#7f8c8d" stroke-width="2" marker-end="url(#smallarrow)"/>
                <path d="M 240 110 L 270 110" stroke="#7f8c8d" stroke-width="2" marker-end="url(#smallarrow)"/>
                <path d="M 390 110 L 420 110" stroke="#7f8c8d" stroke-width="2" marker-end="url(#smallarrow)"/>
                <path d="M 460 110 L 490 110" stroke="#7f8c8d" stroke-width="2" marker-end="url(#smallarrow)"/>
                
                <!-- リダイレクト説明 -->
                <text x="400" y="200" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">リダイレクト（>　>>）</text>
                
                <!-- Output redirection -->
                <rect x="150" y="230" width="150" height="50" fill="#9b59b6" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="225" y="250" text-anchor="middle" fill="white" font-size="14" font-weight="bold">ls -la > file.txt</text>
                <text x="225" y="270" text-anchor="middle" fill="white" font-size="12">ファイルに出力（上書き）</text>
                
                <!-- Append redirection -->
                <rect x="500" y="230" width="150" height="50" fill="#8e44ad" stroke="#2c3e50" stroke-width="2" rx="5"/>
                <text x="575" y="250" text-anchor="middle" fill="white" font-size="14" font-weight="bold">echo "text" >> file.txt</text>
                <text x="575" y="270" text-anchor="middle" fill="white" font-size="12">ファイルに追記</text>
                
                <!-- Example terminal output -->
                <rect x="100" y="320" width="600" height="60" fill="#2c3e50" stroke="#34495e" stroke-width="2"/>
                <text x="110" y="340" fill="#27ae60" font-family="monospace" font-size="12">$ ls -la | grep "\.txt" | wc -l</text>
                <text x="110" y="360" fill="#95a5a6" font-family="monospace" font-size="12">5</text>
                <text x="110" y="375" fill="#7f8c8d" font-size="10">（.txt ファイルの数をカウント）</text>
                
                <!-- Arrow definitions -->
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#2c3e50"/>
                    </marker>
                    <marker id="smallarrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
                        <polygon points="0 0, 8 3, 0 6" fill="#7f8c8d"/>
                    </marker>
                </defs>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>パイプの便利な組み合わせ：</strong>
            <ul>
                <li><code>ps aux | grep プロセス名</code> - 特定プロセスを検索</li>
                <li><code>history | grep コマンド名</code> - コマンド履歴を検索</li>
                <li><code>cat ファイル名 | sort | uniq</code> - 重複除去して並び替え</li>
                <li><code>find . -name "*.log" | xargs rm</code> - 検索結果を削除</li>
            </ul>
        </div>
        
        <h2>2.3 ファイル権限とアクセス制御</h2>
        
        <div class="diagram-container">
            <svg width="800" height="500" viewBox="0 0 800 500">
                <!-- Permission display example -->
                <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">ファイル権限の見方</text>
                
                <!-- Terminal output simulation -->
                <rect x="100" y="50" width="600" height="100" fill="#2c3e50" stroke="#34495e" stroke-width="2"/>
                <text x="110" y="75" fill="#27ae60" font-family="monospace" font-size="14">$ ls -la</text>
                <text x="110" y="95" fill="#95a5a6" font-family="monospace" font-size="12">-rw-r--r--  1 user group  1024 Jan 15 10:30 file.txt</text>
                <text x="110" y="115" fill="#95a5a6" font-family="monospace" font-size="12">drwxr-xr-x  2 user group  4096 Jan 15 10:30 folder</text>
                <text x="110" y="135" fill="#95a5a6" font-family="monospace" font-size="12">-rwx------  1 user group   512 Jan 15 10:30 script.sh</text>
                
                <!-- Permission breakdown -->
                <text x="400" y="180" text-anchor="middle" font-size="18" font-weight="bold" fill="#2c3e50">権限の構成</text>
                
                <!-- File type -->
                <rect x="120" y="200" width="40" height="40" fill="#e74c3c"/>
                <text x="140" y="225" text-anchor="middle" fill="white" font-size="16" font-weight="bold">-</text>
                <text x="140" y="260" text-anchor="middle" font-size="12" fill="#2c3e50">ファイル種別</text>
                <text x="140" y="275" text-anchor="middle" font-size="10" fill="#7f8c8d">- : 通常ファイル</text>
                <text x="140" y="290" text-anchor="middle" font-size="10" fill="#7f8c8d">d : ディレクトリ</text>
                
                <!-- Owner permissions -->
                <rect x="200" y="200" width="120" height="40" fill="#3498db"/>
                <text x="260" y="225" text-anchor="middle" fill="white" font-size="16" font-weight="bold">rwx</text>
                <text x="260" y="260" text-anchor="middle" font-size="12" fill="#2c3e50">所有者の権限</text>
                <text x="230" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">r:読み</text>
                <text x="260" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">w:書き</text>
                <text x="290" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">x:実行</text>
                
                <!-- Group permissions -->
                <rect x="360" y="200" width="120" height="40" fill="#f39c12"/>
                <text x="420" y="225" text-anchor="middle" fill="white" font-size="16" font-weight="bold">r-x</text>
                <text x="420" y="260" text-anchor="middle" font-size="12" fill="#2c3e50">グループの権限</text>
                <text x="390" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">r:読み</text>
                <text x="420" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">-:書込不可</text>
                <text x="450" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">x:実行</text>
                
                <!-- Other permissions -->
                <rect x="520" y="200" width="120" height="40" fill="#27ae60"/>
                <text x="580" y="225" text-anchor="middle" fill="white" font-size="16" font-weight="bold">r--</text>
                <text x="580" y="260" text-anchor="middle" font-size="12" fill="#2c3e50">その他の権限</text>
                <text x="550" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">r:読み</text>
                <text x="580" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">-:書込不可</text>
                <text x="610" y="280" text-anchor="middle" font-size="10" fill="#7f8c8d">-:実行不可</text>
                
                <!-- Numeric representation -->
                <text x="400" y="330" text-anchor="middle" font-size="18" font-weight="bold" fill="#2c3e50">数値表記</text>
                
                <!-- chmod examples -->
                <rect x="150" y="350" width="150" height="60" fill="#9b59b6"/>
                <text x="225" y="375" text-anchor="middle" fill="white" font-size="14" font-weight="bold">chmod 755</text>
                <text x="225" y="395" text-anchor="middle" fill="white" font-size="12">rwxr-xr-x</text>
                
                <rect x="350" y="350" width="150" height="60" fill="#e67e22"/>
                <text x="425" y="375" text-anchor="middle" fill="white" font-size="14" font-weight="bold">chmod 644</text>
                <text x="425" y="395" text-anchor="middle" fill="white" font-size="12">rw-r--r--</text>
                
                <rect x="550" y="350" width="150" height="60" fill="#1abc9c"/>
                <text x="625" y="375" text-anchor="middle" fill="white" font-size="14" font-weight="bold">chmod 600</text>
                <text x="625" y="395" text-anchor="middle" fill="white" font-size="12">rw-------</text>
                
                <!-- Number meanings -->
                <text x="400" y="440" text-anchor="middle" font-size="14" fill="#2c3e50">4=読み　2=書き　1=実行</text>
                <text x="400" y="460" text-anchor="middle" font-size="12" fill="#7f8c8d">7=4+2+1(全権限)　5=4+1(読み・実行)　4=読みのみ</text>
            </svg>
        </div>
        
        <div class="command-grid">
            <div class="command-card">
                <h3>chmod - 権限変更</h3>
                <div class="command-box">$ chmod 755 script.sh</div>
                <div class="command-box">$ chmod +x program</div>
                <p>よく使う権限：</p>
                <ul>
                    <li>755: 実行可能ファイル</li>
                    <li>644: 通常ファイル</li>
                    <li>600: 秘密ファイル（自分のみ）</li>
                </ul>
            </div>
            
            <div class="command-card">
                <h3>chown - 所有者変更</h3>
                <div class="command-box">$ chown user:group file.txt</div>
                <div class="command-box">$ chown -R user:group directory/</div>
                <p><code>-R</code>: 再帰的に変更（ディレクトリ内すべて）</p>
                <p><strong>注意：</strong>通常は管理者権限（sudo）が必要</p>
            </div>
        </div>
        
        <h2>2.4 プロセス管理</h2>
        
        <div class="diagram-container">
            <svg width="800" height="450" viewBox="0 0 800 450">
                <!-- Process overview -->
                <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#2c3e50">プロセス管理の全体像</text>
                
                <!-- Terminal showing ps output -->
                <rect x="50" y="50" width="700" height="120" fill="#2c3e50" stroke="#34495e" stroke-width="2"/>
                <text x="60" y="75" fill="#27ae60" font-family="monospace" font-size="12">$ ps aux</text>
                <text x="60" y="95" fill="#95a5a6" font-family="monospace" font-size="10">USER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND</text>
                <text x="60" y="110" fill="#95a5a6" font-family="monospace" font-size="10">root         1   0.0  0.1  225344  4624 ?        Ss   10:30   0:01 /sbin/init</text>
                <text x="60" y="125" fill="#95a5a6" font-family="monospace" font-size="10">user      1234   1.5  2.1  123456 12345 pts/0    S+   10:45   0:03 python app.py</text>
                <text x="60" y="140" fill="#95a5a6" font-family="monospace" font-size="10">user      5678   0.2  0.5   45678  2345 pts/1    R+   10:50   0:00 top</text>
                <text x="60" y="155" fill="#95a5a6" font-family="monospace" font-size="10">user      9999  25.3  5.8  987654 56789 ?        R    10:52   1:23 heavy_process</text>
                
                <!-- Process states -->
                <text x="400" y="200" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">プロセスの状態</text>
                
                <!-- Running -->
                <rect x="100" y="220" width="100" height="50" fill="#27ae60"/>
                <text x="150" y="240" text-anchor="middle" fill="white" font-size="12" font-weight="bold">実行中</text>
                <text x="150" y="255" text-anchor="middle" fill="white" font-size="10">Running (R)</text>
                
                <!-- Sleeping -->
                <rect x="250" y="220" width="100" height="50" fill="#3498db"/>
                <text x="300" y="240" text-anchor="middle" fill="white" font-size="12" font-weight="bold">待機中</text>
                <text x="300" y="255" text-anchor="middle" fill="white" font-size="10">Sleeping (S)</text>
                
                <!-- Stopped -->
                <rect x="400" y="220" width="100" height="50" fill="#f39c12"/>
                <text x="450" y="240" text-anchor="middle" fill="white" font-size="12" font-weight="bold">停止</text>
                <text x="450" y="255" text-anchor="middle" fill="white" font-size="10">Stopped (T)</text>
                
                <!-- Zombie -->
                <rect x="550" y="220" width="100" height="50" fill="#e74c3c"/>
                <text x="600" y="240" text-anchor="middle" fill="white" font-size="12" font-weight="bold">ゾンビ</text>
                <text x="600" y="255" text-anchor="middle" fill="white" font-size="10">Zombie (Z)</text>
                
                <!-- Process control -->
                <text x="400" y="300" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">プロセス制御</text>
                
                <!-- Kill process -->
                <rect x="150" y="320" width="150" height="40" fill="#c0392b"/>
                <text x="225" y="345" text-anchor="middle" fill="white" font-size="12">kill 1234</text>
                
                <!-- Force kill -->
                <rect x="350" y="320" width="150" height="40" fill="#8e44ad"/>
                <text x="425" y="345" text-anchor="middle" fill="white" font-size="12">kill -9 1234</text>
                
                <!-- Background job -->
                <rect x="550" y="320" width="150" height="40" fill="#16a085"/>
                <text x="625" y="345" text-anchor="middle" fill="white" font-size="12">command &</text>
                
                <!-- Arrows showing process lifecycle -->
                <path d="M 200 245 L 250 245" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 350 245 L 400 245" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 500 245 L 550 245" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                
                <!-- Labels -->
                <text x="225" y="285" text-anchor="middle" font-size="10" fill="#7f8c8d">I/O待ち</text>
                <text x="375" y="285" text-anchor="middle" font-size="10" fill="#7f8c8d">シグナル</text>
                <text x="525" y="285" text-anchor="middle" font-size="10" fill="#7f8c8d">親プロセス待ち</text>
                
                <!-- Real-time monitoring -->
                <text x="400" y="400" text-anchor="middle" font-size="14" font-weight="bold" fill="#2c3e50">リアルタイム監視: top / htop</text>
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