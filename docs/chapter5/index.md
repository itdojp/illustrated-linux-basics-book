---
layout: chapter
title: "第5章：実践練習"
chapter: 5
---

<div class="section">
    <h1>第5章：実践練習</h1>
    
    <h2>5.1 環境構築の流れ</h2>
    
    <div class="practice-step">
        <h4>ステップ1: システム情報確認</h4>
        <div class="command-box">$ uname -a</div>
        <div class="command-box">$ lsb_release -a</div>
        <div class="command-box">$ free -h && df -h</div>
        <p>OSの種類、バージョン、リソース状況を確認</p>
    </div>
    
    <div class="practice-step">
        <h4>ステップ2: パッケージ管理</h4>
        <div class="command-box">$ sudo apt update && sudo apt upgrade</div>
        <div class="command-box">$ sudo apt install git vim curl</div>
        <p>システムを最新状態にし、必要なツールをインストール</p>
    </div>
    
    <div class="practice-step">
        <h4>ステップ3: ユーザー・権限設定</h4>
        <div class="command-box">$ sudo useradd -m developer</div>
        <div class="command-box">$ sudo usermod -aG sudo developer</div>
        <div class="command-box">$ chmod 755 ~/projects</div>
        <p>開発用ユーザーを作成し、適切な権限を設定</p>
    </div>
    
    <h2>5.2 Webサーバー構築</h2>
    
    <div class="container-example">
        <h4>Apache2のインストールと設定</h4>
        <div class="command-box">$ sudo apt install apache2</div>
        <div class="command-box">$ sudo systemctl enable apache2</div>
        <div class="command-box">$ sudo systemctl start apache2</div>
        <div class="command-box">$ sudo systemctl status apache2</div>
        <p>Webサーバーを起動し、自動起動を有効化</p>
    </div>
    
    <div class="container-example">
        <h4>ファイアウォール設定</h4>
        <div class="command-box">$ sudo ufw allow 'Apache Full'</div>
        <div class="command-box">$ sudo ufw enable</div>
        <div class="command-box">$ sudo ufw status</div>
        <p>HTTP/HTTPSポートを開放</p>
    </div>
    
    <h2>5.3 監視・ログ管理</h2>
    
    <div class="command-grid">
        <div class="command-card">
            <h3>システム監視</h3>
            <div class="command-box">$ top</div>
            <div class="command-box">$ htop</div>
            <div class="command-box">$ iotop</div>
            <p>CPU、メモリ、ディスクI/Oを監視</p>
        </div>
        
        <div class="command-card">
            <h3>ログ確認</h3>
            <div class="command-box">$ sudo journalctl -f</div>
            <div class="command-box">$ tail -f /var/log/apache2/access.log</div>
            <div class="command-box">$ grep "ERROR" /var/log/syslog</div>
            <p>システムとアプリケーションのログを確認</p>
        </div>
        
        <div class="command-card">
            <h3>ネットワーク診断</h3>
            <div class="command-box">$ ss -tuln</div>
            <div class="command-box">$ ping -c 4 google.com</div>
            <div class="command-box">$ curl -I http://localhost</div>
            <p>サービスの稼働状況を確認</p>
        </div>
        
        <div class="command-card">
            <h3>自動化・スクリプト</h3>
            <div class="command-box">$ crontab -e</div>
            <div class="command-box">#!/bin/bash<br>echo "Backup completed"</div>
            <div class="command-box">$ chmod +x backup.sh</div>
            <p>定期実行とシェルスクリプト</p>
        </div>
    </div>
    
    <h2>5.4 トラブルシューティング</h2>
    
    <div class="warning">
        <strong>よくある問題と対処法</strong>
        <ul>
            <li><strong>Permission denied</strong> → <code>sudo</code>を使うか、<code>chmod</code>で権限変更</li>
            <li><strong>Command not found</strong> → <code>which</code>でパス確認、パッケージインストール</li>
            <li><strong>Port already in use</strong> → <code>ss -tuln</code>で使用ポート確認、プロセス停止</li>
            <li><strong>Disk space</strong> → <code>df -h</code>で容量確認、<code>du -sh *</code>で使用量調査</li>
        </ul>
    </div>
    
    <div class="success">
        <h4>総復習チェックリスト</h4>
        <ul>
            <li>□ 基本コマンド（ls, cd, mkdir, rm, cp, mv）が使える</li>
            <li>□ ファイル権限（chmod, chown）が理解できている</li>
            <li>□ プロセス管理（ps, kill, jobs）ができる</li>
            <li>□ ネットワーク診断（ping, curl, netstat）ができる</li>
            <li>□ パッケージ管理（apt, yum）が使える</li>
            <li>□ サービス管理（systemctl, service）が理解できている</li>
            <li>□ ログファイルの確認方法を知っている</li>
            <li>□ 基本的なトラブルシューティングができる</li>
        </ul>
    </div>
    
    <div class="key-point">
        <strong>次のステップ：</strong>
        <ul>
            <li>シェルスクリプトを学んで作業を自動化</li>
            <li>Dockerを使ったアプリケーション管理</li>
            <li>CI/CDパイプラインの構築</li>
            <li>クラウド環境でのLinux運用</li>
        </ul>
    </div>
</div>