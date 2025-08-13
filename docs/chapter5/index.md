---
layout: chapter
title: "第5章：実践演習 - 簡単なスクリプト作成"
chapter: 5
---

<div class="section">
    <h1>第5章：実践演習 - 簡単なスクリプト作成</h1>
    
    <h2>5.1 はじめてのシェルスクリプト</h2>
    
    <div class="explanation">
        <h3>シェルスクリプトとは？</h3>
        <p>コマンドを順番に実行するプログラムです。繰り返し作業を自動化できます。</p>
    </div>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>最初のスクリプト: hello.sh</h3>
            <div class="command-box">
$ nano hello.sh
            </div>
            <div class="code-box">
#!/bin/bash
# これはコメントです
echo "Hello, Linux World!"
echo "今日は $(date) です"
            </div>
            <div class="command-box">
$ chmod +x hello.sh  # 実行権限を付与<br>
$ ./hello.sh  # 実行
            </div>
            <div class="output-box">
Hello, Linux World!<br>
今日は Mon Jan 15 10:30:45 JST 2025 です
            </div>
        </div>
    </div>
    
    <h2>5.2 バックアップスクリプトを作ろう</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>backup.sh - 重要ファイルのバックアップ</h3>
            <div class="code-box">
#!/bin/bash

# バックアップ元とバックアップ先
SOURCE="$HOME/Documents"
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${DATE}.tar.gz"

# バックアップディレクトリ作成
mkdir -p "$BACKUP_DIR"

# バックアップ実行
echo "バックアップを開始します..."
tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE" 2>/dev/null

# 結果確認
if [ $? -eq 0 ]; then
    echo "✅ バックアップ成功: $BACKUP_FILE"
    ls -lh "$BACKUP_DIR/$BACKUP_FILE"
else
    echo "❌ バックアップ失敗"
    exit 1
fi

# 古いバックアップを削除（7日以上前）
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete
echo "7日以上前のバックアップを削除しました"
            </div>
            <p><strong>使い方：</strong></p>
            <div class="command-box">
$ chmod +x backup.sh<br>
$ ./backup.sh
            </div>
        </div>
    </div>
    
    <h2>5.3 システム情報レポート作成</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>sysinfo.sh - システム状態レポート</h3>
            <div class="code-box">
#!/bin/bash

echo "========================================="
echo "     システム情報レポート"
echo "     作成日時: $(date)"
echo "========================================="
echo ""

echo "【ホスト情報】"
echo "ホスト名: $(hostname)"
echo "OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
echo "カーネル: $(uname -r)"
echo ""

echo "【CPU情報】"
echo "CPU: $(lscpu | grep 'Model name' | cut -d':' -f2 | xargs)"
echo "コア数: $(nproc)"
echo ""

echo "【メモリ情報】"
free -h | grep Mem | awk '{print "総メモリ: "$2"\n使用中: "$3"\n空き: "$4}'
echo ""

echo "【ディスク使用状況】"
df -h | grep -E '^/dev/' | awk '{print $1": "$5" 使用 ("$3"/"$2")"}'
echo ""

echo "【ネットワーク】"
ip -4 addr | grep inet | grep -v 127.0.0.1 | awk '{print "IP: "$2}'
echo ""

echo "【起動時間】"
uptime -p
echo ""

echo "レポート作成完了"
            </div>
            <p><strong>実行例：</strong></p>
            <div class="command-box">
$ chmod +x sysinfo.sh<br>
$ ./sysinfo.sh > report.txt  # ファイルに保存
            </div>
        </div>
    </div>
    
    <h2>5.4 ファイル整理スクリプト</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>organize.sh - ダウンロードフォルダ整理</h3>
            <div class="code-box">
#!/bin/bash

# 整理対象ディレクトリ
TARGET_DIR="$HOME/Downloads"
cd "$TARGET_DIR" || exit 1

echo "📁 ダウンロードフォルダを整理します..."

# 各種フォルダを作成
mkdir -p Images Documents Videos Archives Others

# 画像ファイルを移動
for file in *.{jpg,jpeg,png,gif,svg,webp} 2>/dev/null; do
    [ -f "$file" ] && mv "$file" Images/ && echo "  画像: $file → Images/"
done

# ドキュメントを移動
for file in *.{pdf,doc,docx,txt,odt} 2>/dev/null; do
    [ -f "$file" ] && mv "$file" Documents/ && echo "  文書: $file → Documents/"
done

# 動画を移動
for file in *.{mp4,avi,mkv,mov,webm} 2>/dev/null; do
    [ -f "$file" ] && mv "$file" Videos/ && echo "  動画: $file → Videos/"
done

# アーカイブを移動
for file in *.{zip,tar,gz,7z,rar} 2>/dev/null; do
    [ -f "$file" ] && mv "$file" Archives/ && echo "  圧縮: $file → Archives/"
done

echo "✅ 整理完了！"
            </div>
        </div>
    </div>
    
    <h2>5.5 便利な関数とエイリアス</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>.bashrc に追加する便利設定</h3>
            <div class="code-box">
# ~/.bashrc に追加

# よく使うコマンドのエイリアス
alias ll='ls -la'
alias ..='cd ..'
alias ...='cd ../..'
alias grep='grep --color=auto'
alias df='df -h'
alias free='free -h'

# 安全対策
alias rm='rm -i'  # 削除前に確認
alias cp='cp -i'  # 上書き前に確認
alias mv='mv -i'  # 移動前に確認

# ディレクトリ作成して移動する関数
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# ファイル検索関数
findfile() {
    find . -type f -name "*$1*" 2>/dev/null
}

# プロセス検索関数
psgrep() {
    ps aux | grep -v grep | grep "$1"
}

# 解凍万能関数
extract() {
    if [ -f "$1" ]; then
        case "$1" in
            *.tar.gz)  tar xzf "$1"    ;;
            *.tar.bz2) tar xjf "$1"    ;;
            *.zip)     unzip "$1"      ;;
            *.gz)      gunzip "$1"     ;;
            *.tar)     tar xf "$1"     ;;
            *.tgz)     tar xzf "$1"    ;;
            *)         echo "未対応の形式: $1" ;;
        esac
    else
        echo "ファイルが見つかりません: $1"
    fi
}
            </div>
            <p><strong>設定を反映：</strong></p>
            <div class="command-box">$ source ~/.bashrc</div>
        </div>
    </div>
    
    <h2>5.6 cronで定期実行</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>定期バックアップの設定</h3>
            <div class="command-box">$ crontab -e</div>
            <div class="code-box">
# 毎日午前3時にバックアップ実行
0 3 * * * /home/user/scripts/backup.sh

# 毎週月曜日にシステムレポート作成
0 9 * * 1 /home/user/scripts/sysinfo.sh > /home/user/weekly_report.txt

# 毎月1日に古いログを削除
0 0 1 * * find /home/user/logs -name "*.log" -mtime +30 -delete
            </div>
            <h4>cron記法の説明</h4>
            <div class="explanation">
                <pre>
分 時 日 月 曜日 コマンド
*  *  *  *  *    command

例：
*/5 * * * *  5分ごと
0 */2 * * *  2時間ごと
0 9-17 * * 1-5  平日9-17時の毎時0分
                </pre>
            </div>
        </div>
    </div>
    
    <h2>5.7 学習のまとめ</h2>
    
    <div class="explanation">
        <h3>🎯 この章で学んだこと</h3>
        <ul>
            <li>シェルスクリプトの基本構造</li>
            <li>変数とコマンド置換の使い方</li>
            <li>条件分岐（if文）の基本</li>
            <li>ループ処理（for文）の基本</li>
            <li>関数の定義と使用</li>
            <li>cronによる定期実行</li>
        </ul>
        
        <h3>📚 次のステップ</h3>
        <ul>
            <li>より複雑な条件分岐（case文）</li>
            <li>配列の使用</li>
            <li>エラーハンドリング</li>
            <li>デバッグ技法</li>
            <li>sedやawkを使った高度なテキスト処理</li>
        </ul>
        
        <h3>💡 スクリプト作成のコツ</h3>
        <ul>
            <li><strong>小さく始める</strong>：まず簡単な処理から作る</li>
            <li><strong>コメントを書く</strong>：後で見返した時のために</li>
            <li><strong>エラー処理を入れる</strong>：想定外の状況に備える</li>
            <li><strong>テストする</strong>：本番前に必ずテスト環境で実行</li>
            <li><strong>バージョン管理</strong>：gitなどで管理する</li>
        </ul>
    </div>
    
    <div class="important-note">
        <h3>⚠️ セキュリティの注意点</h3>
        <ul>
            <li>パスワードをスクリプトに直接書かない</li>
            <li>実行権限は必要最小限に</li>
            <li>入力値の検証を行う</li>
            <li>rm -rf などの危険なコマンドは慎重に</li>
        </ul>
    </div>
</div>