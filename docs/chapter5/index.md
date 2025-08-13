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
    
    <h2>5.2 実践！バックアップスクリプト</h2>
    
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
    
    <h2>5.3 cronで定期実行</h2>
    
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
    
    <h2>5.4 学習のまとめ</h2>
    
    <div class="explanation">
        <h3>🎯 この章で学んだこと</h3>
        <ul>
            <li>シェルスクリプトの基本構造（#!/bin/bash）</li>
            <li>変数の定義と使用方法</li>
            <li>条件分岐（if文）による処理制御</li>
            <li>コマンド置換（$(command)）の活用</li>
            <li>cronによる定期実行の設定</li>
        </ul>
        
        <h3>📚 次のステップ</h3>
        <ul>
            <li>ループ処理（for, while文）の学習</li>
            <li>関数の定義と活用</li>
            <li>より複雑な条件分岐（case文）</li>
            <li>エラーハンドリングの実装</li>
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