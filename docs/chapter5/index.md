---
layout: chapter
title: "第5章：実践演習 - 簡単なスクリプト作成"
chapter: 5
---

<div class="section">
    <h1>第5章：実践演習 - 簡単なスクリプト作成</h1>
    
    <h2>5.0 この章で学ぶこと</h2>
    
    <div class="explanation">
        <ul>
            <li>シェルスクリプトの最小構成（shebang/コメント/コマンド実行）を作れる</li>
            <li><code>tar</code> や <code>find</code> を使った簡単な自動化の例を理解できる</li>
            <li><code>cron</code> で定期実行できる</li>
        </ul>
    </div>
    
    <h2>5.1 はじめてのシェルスクリプト</h2>
    
    <div class="explanation">
        <h3>シェルスクリプトの概要</h3>
        <p>コマンドを順番に実行するプログラムです。繰り返し作業を自動化できます。</p>
    </div>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>最初のスクリプト: hello.sh</h3>
            <pre class="command-box"><code class="language-bash">$ vi hello.sh</code></pre>
            <pre class="code-box"><code class="language-bash">&#35;!/usr/bin/env bash
&#35; これはコメントです
echo "Hello, Linux World!"
echo "今日は $(date) です"</code></pre>
            <pre class="command-box"><code class="language-bash">$ chmod +x hello.sh  # 実行権限を付与
$ ./hello.sh  # 実行</code></pre>
            <pre class="output-box"><code class="language-text">Hello, Linux World!
今日は Mon Jan 15 10:30:45 JST 2025 です</code></pre>
        </div>
    </div>
    
    <h2>5.2 実践: バックアップスクリプト</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>backup.sh - 重要ファイルのバックアップ</h3>
            <pre class="code-box"><code class="language-bash">&#35;!/usr/bin/env bash

&#35; バックアップ元とバックアップ先
SOURCE="$HOME/Documents"
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${DATE}.tar.gz"

&#35; バックアップディレクトリ作成
mkdir -p "$BACKUP_DIR"

&#35; バックアップ実行
echo "バックアップを開始します"
tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE"

&#35; 結果確認
if [ $? -eq 0 ]; then
    echo "バックアップ成功: $BACKUP_FILE"
    ls -lh "$BACKUP_DIR/$BACKUP_FILE"
else
    echo "バックアップ失敗"
    exit 1
fi

&#35; 古いバックアップを削除（7日以上前）
&#35; [注意] まずは削除対象を確認したい場合は、以下の確認用コマンドを実行する
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -print
&#35; 確認後に削除したい場合は、次のコマンドを実行する
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete
echo "7日以上前のバックアップを削除しました（該当がある場合）"</code></pre>
            <p><strong>使い方：</strong></p>
            <pre class="command-box"><code class="language-bash">$ chmod +x backup.sh
$ ./backup.sh</code></pre>
        </div>
    </div>
    
    <h2>5.3 cronで定期実行</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>定期バックアップの設定</h3>
            <pre class="command-box"><code class="language-bash">$ crontab -e</code></pre>
            <pre class="code-box"><code class="language-text">&#35; 毎日午前3時にバックアップ実行
0 3 * * * /home/user/scripts/backup.sh

&#35; 毎週月曜日にシステムレポート作成
0 9 * * 1 /home/user/scripts/sysinfo.sh > /home/user/weekly_report.txt

&#35; 毎月1日に古いログを削除
0 0 1 * * find /home/user/logs -name "*.log" ! -name "cron.log" -mtime +30 -print -delete >> /home/user/logs/cron.log 2>&1</code></pre>
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
            <div class="key-point">
                <strong>補足：</strong>cron は対話シェルと実行環境が異なります。注意点は次のとおりです。
                <ul>
                    <li>PATH が最小限のため、必要ならフルパス（例: <code>/usr/bin/python3</code>）を使う</li>
                    <li>環境変数が引き継がれないため、必要な変数は crontab 側で定義する</li>
                    <li>標準出力/標準エラーはログへリダイレクトし、失敗時に追跡できるようにする</li>
                </ul>
            </div>
        </div>
    </div>
    
    <h2>5.4 学習のまとめ</h2>
    
    <div class="explanation">
        <h3>この章で学んだこと</h3>
        <ul>
            <li>シェルスクリプトの基本構造（shebang/コメント/実行権限）</li>
            <li>変数の定義と使用方法</li>
            <li>条件分岐（if文）による処理制御</li>
            <li>コマンド置換（$(command)）の活用</li>
            <li>cronによる定期実行の設定</li>
        </ul>
        
        <h3>次のステップ</h3>
        <ul>
            <li>ループ処理（for, while文）の学習</li>
            <li>関数の定義と活用</li>
            <li>より複雑な条件分岐（case文）</li>
            <li>エラーハンドリングの実装</li>
        </ul>
        
        <h3>スクリプト作成の要点</h3>
        <ul>
            <li><strong>小さく始める</strong>：まず簡単な処理から作る</li>
            <li><strong>コメントを書く</strong>：後で見返したときのために</li>
            <li><strong>エラー処理を入れる</strong>：想定外の状況に備える</li>
            <li><strong>テストする</strong>：本番前に必ずテスト環境で実行</li>
            <li><strong>バージョン管理</strong>：Git などで管理する</li>
        </ul>
    </div>
    
    <div class="important-note">
        <h3>セキュリティの注意点</h3>
        <ul>
            <li>パスワードをスクリプトに直接書かない</li>
            <li>実行権限は必要最小限に</li>
            <li>入力値の検証を行う</li>
            <li>rm -rf などの危険なコマンドは慎重に</li>
        </ul>
    </div>

    <div class="key-point">
        <strong>次に読む：</strong>
        <ul>
            <li><a href="../appendix/">付録：コマンド一覧表</a>（必要に応じてコマンドを確認する）</li>
            <li><a href="../">目次</a>（目的の章に戻る）</li>
        </ul>
    </div>
</div>
