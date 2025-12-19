---
layout: chapter
title: "第0章：コンピュータの仕組み"
chapter: 0
---

<div class="section">
        <h1>第0章：コンピュータの仕組み</h1>
        
        <h2>0.0 この章で学ぶこと</h2>
        
        <div class="explanation">
            <ul>
                <li>CPU・メモリ・ストレージなど、PCの主要パーツの役割を説明できる</li>
                <li>OSが「アプリとハードウェアの間」をつなぐ理由を説明できる</li>
                <li>サーバーが「役割」であること（通常のPCとの違い）を説明できる</li>
            </ul>
        </div>
        
        <h2>0.1 PCの中身を図解</h2>
        
        <div class="diagram-container">
            <svg width="800" height="500" viewBox="0 0 800 500">
                <!-- CPU -->
                <rect x="50" y="50" width="150" height="150" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                <text x="125" y="130" text-anchor="middle" fill="white" font-size="20" font-weight="bold">CPU</text>
                <text x="125" y="150" text-anchor="middle" fill="white" font-size="12">脳みそ</text>
                <text x="125" y="170" text-anchor="middle" fill="white" font-size="12">（計算担当）</text>
                
                <!-- Memory -->
                <rect x="250" y="50" width="150" height="150" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                <text x="325" y="130" text-anchor="middle" fill="white" font-size="20" font-weight="bold">メモリ</text>
                <text x="325" y="150" text-anchor="middle" fill="white" font-size="12">作業台</text>
                <text x="325" y="170" text-anchor="middle" fill="white" font-size="12">（一時記憶）</text>
                
                <!-- Storage -->
                <rect x="450" y="50" width="150" height="150" fill="#2ecc71" stroke="#2c3e50" stroke-width="2"/>
                <text x="525" y="130" text-anchor="middle" fill="white" font-size="20" font-weight="bold">ストレージ</text>
                <text x="525" y="150" text-anchor="middle" fill="white" font-size="12">倉庫</text>
                <text x="525" y="170" text-anchor="middle" fill="white" font-size="12">（永続保存）</text>
                
                <!-- Motherboard -->
                <rect x="650" y="50" width="120" height="150" fill="#9b59b6" stroke="#2c3e50" stroke-width="2"/>
                <text x="710" y="130" text-anchor="middle" fill="white" font-size="16" font-weight="bold">マザーボード</text>
                <text x="710" y="150" text-anchor="middle" fill="white" font-size="12">土台</text>
                <text x="710" y="170" text-anchor="middle" fill="white" font-size="12">（全体を繋ぐ）</text>
                
                <!-- 料理の例え -->
                <g transform="translate(0, 250)">
                    <text x="50" y="0" font-size="18" font-weight="bold" fill="#2c3e50">料理に例えると...</text>
                    
                    <!-- CPU = シェフ -->
                    <circle cx="125" cy="80" r="40" fill="#3498db" opacity="0.8"/>
                    <text x="125" y="85" text-anchor="middle" fill="white" font-size="14">シェフ</text>
                    <text x="125" y="140" text-anchor="middle" font-size="12">調理する人</text>
                    
                    <!-- メモリ = まな板 -->
                    <rect x="275" y="50" width="100" height="60" fill="#e74c3c" opacity="0.8" rx="5"/>
                    <text x="325" y="85" text-anchor="middle" fill="white" font-size="14">まな板</text>
                    <text x="325" y="140" text-anchor="middle" font-size="12">作業スペース</text>
                    
                    <!-- ストレージ = 冷蔵庫 -->
                    <rect x="475" y="40" width="100" height="80" fill="#2ecc71" opacity="0.8"/>
                    <text x="525" y="85" text-anchor="middle" fill="white" font-size="14">冷蔵庫</text>
                    <text x="525" y="140" text-anchor="middle" font-size="12">材料を保管</text>
                    
                    <!-- マザーボード = キッチン -->
                    <rect x="650" y="30" width="120" height="100" fill="#9b59b6" opacity="0.3" stroke="#9b59b6" stroke-width="2"/>
                    <text x="710" y="85" text-anchor="middle" fill="#9b59b6" font-size="14">キッチン全体</text>
                    <text x="710" y="140" text-anchor="middle" font-size="12">全てが置かれる場所</text>
                </g>
                
                <!-- 矢印で関係性を示す -->
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#7f8c8d"/>
                    </marker>
                </defs>
                
                <path d="M 200 125 L 250 125" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 400 125 L 450 125" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 600 125 L 650 125" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>動作の流れ：</strong>
            <ol>
                <li>ストレージ（HDD/SSD）からプログラムとデータを取り出す</li>
                <li>メモリ（RAM）に一時的に置く</li>
                <li>CPU が メモリ上のデータを処理</li>
                <li>結果をメモリに書き戻し、必要に応じてストレージに保存</li>
            </ol>
        </div>
        
        <h2>0.2 OSとは何か</h2>
        
        <div class="diagram-container">
            <svg width="800" height="400" viewBox="0 0 800 400">
                <!-- ハードウェア層 -->
                <rect x="50" y="300" width="700" height="80" fill="#95a5a6" stroke="#2c3e50" stroke-width="2"/>
                <text x="400" y="345" text-anchor="middle" fill="white" font-size="18" font-weight="bold">ハードウェア（CPU、メモリ、ディスク等）</text>
                
                <!-- OS層 -->
                <rect x="50" y="180" width="700" height="100" fill="#3498db" stroke="#2c3e50" stroke-width="2"/>
                <text x="400" y="220" text-anchor="middle" fill="white" font-size="20" font-weight="bold">オペレーティングシステム（OS）</text>
                <text x="400" y="250" text-anchor="middle" fill="white" font-size="14">ハードウェアとアプリケーションの仲介役</text>
                
                <!-- アプリケーション層 -->
                <g>
                    <rect x="80" y="50" width="120" height="100" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="140" y="105" text-anchor="middle" fill="white" font-size="14">ブラウザ</text>
                    
                    <rect x="240" y="50" width="120" height="100" fill="#2ecc71" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="300" y="105" text-anchor="middle" fill="white" font-size="14">エディタ</text>
                    
                    <rect x="400" y="50" width="120" height="100" fill="#f39c12" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="460" y="105" text-anchor="middle" fill="white" font-size="14">データベース</text>
                    
                    <rect x="560" y="50" width="120" height="100" fill="#9b59b6" stroke="#2c3e50" stroke-width="2" rx="5"/>
                    <text x="620" y="105" text-anchor="middle" fill="white" font-size="14">Webサーバー</text>
                </g>
                
                <!-- 矢印 -->
                <path d="M 140 150 L 140 180" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 300 150 L 300 180" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 460 150 L 460 180" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                <path d="M 620 150 L 620 180" stroke="#7f8c8d" stroke-width="2" marker-end="url(#arrowhead)"/>
                
                <path d="M 400 280 L 400 300" stroke="#7f8c8d" stroke-width="3" marker-end="url(#arrowhead)"/>
                
                <!-- ラベル -->
                <text x="30" y="105" text-anchor="middle" font-size="14" fill="#2c3e50" transform="rotate(-90 30 105)">アプリケーション</text>
                <text x="30" y="230" text-anchor="middle" font-size="14" fill="#2c3e50" transform="rotate(-90 30 230)">OS</text>
                <text x="30" y="340" text-anchor="middle" font-size="14" fill="#2c3e50" transform="rotate(-90 30 340)">ハードウェア</text>
            </svg>
        </div>
        
        <div class="key-point">
            <strong>OSの役割：</strong>アプリケーションがハードウェアを直接操作しなくて済むように、標準的なインターフェースを提供する「通訳」のような役割を持ちます。たとえば、アプリケーションは「ファイルを保存したい」とOSに伝えるだけで、どのディスクにどう書き込むかといった細かい処理はOSが代わりに行います。
        </div>
        
        <h2>0.3 サーバーとは</h2>
        
        <div class="diagram-container">
            <svg width="800" height="450" viewBox="0 0 800 450">
                <!-- 通常のPC -->
                <g transform="translate(100, 50)">
                    <rect x="0" y="0" width="200" height="150" fill="#3498db" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="100" y="30" text-anchor="middle" fill="white" font-size="18" font-weight="bold">通常のPC</text>
                    
                    <rect x="20" y="50" width="160" height="20" fill="white" opacity="0.3"/>
                    <text x="100" y="65" text-anchor="middle" fill="white" font-size="12">画面・キーボード必須</text>
                    
                    <rect x="20" y="80" width="160" height="20" fill="white" opacity="0.3"/>
                    <text x="100" y="95" text-anchor="middle" fill="white" font-size="12">1人が使用</text>
                    
                    <rect x="20" y="110" width="160" height="20" fill="white" opacity="0.3"/>
                    <text x="100" y="125" text-anchor="middle" fill="white" font-size="12">電源OFF OK</text>
                </g>
                
                <!-- サーバー -->
                <g transform="translate(450, 50)">
                    <rect x="0" y="0" width="200" height="150" fill="#e74c3c" stroke="#2c3e50" stroke-width="2" rx="10"/>
                    <text x="100" y="30" text-anchor="middle" fill="white" font-size="18" font-weight="bold">サーバー</text>
                    
                    <rect x="20" y="50" width="160" height="20" fill="white" opacity="0.3"/>
                    <text x="100" y="65" text-anchor="middle" fill="white" font-size="12">画面なしでOK</text>
                    
                    <rect x="20" y="80" width="160" height="20" fill="white" opacity="0.3"/>
                    <text x="100" y="95" text-anchor="middle" fill="white" font-size="12">多数が同時利用</text>
                    
                    <rect x="20" y="110" width="160" height="20" fill="white" opacity="0.3"/>
                    <text x="100" y="125" text-anchor="middle" fill="white" font-size="12">24時間365日稼働</text>
                </g>
                
                <!-- ネットワーク接続 -->
                <g transform="translate(0, 250)">
                    <text x="400" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2c3e50">サーバーの使われ方</text>
                    
                    <!-- サーバー（中央） -->
                    <rect x="350" y="40" width="100" height="80" fill="#e74c3c" stroke="#2c3e50" stroke-width="2"/>
                    <text x="400" y="85" text-anchor="middle" fill="white" font-size="14">サーバー</text>
                    
                    <!-- クライアント -->
                    <circle cx="150" cy="80" r="30" fill="#3498db"/>
                    <text x="150" y="85" text-anchor="middle" fill="white" font-size="12">PC</text>
                    
                    <circle cx="250" cy="140" r="30" fill="#3498db"/>
                    <text x="250" y="145" text-anchor="middle" fill="white" font-size="12">スマホ</text>
                    
                    <circle cx="550" cy="140" r="30" fill="#3498db"/>
                    <text x="550" y="145" text-anchor="middle" fill="white" font-size="12">タブレット</text>
                    
                    <circle cx="650" cy="80" r="30" fill="#3498db"/>
                    <text x="650" y="85" text-anchor="middle" fill="white" font-size="12">PC</text>
                    
                    <!-- 接続線 -->
                    <line x1="180" y1="80" x2="350" y2="80" stroke="#7f8c8d" stroke-width="2"/>
                    <line x1="280" y1="140" x2="370" y2="100" stroke="#7f8c8d" stroke-width="2"/>
                    <line x1="520" y1="140" x2="430" y2="100" stroke="#7f8c8d" stroke-width="2"/>
                    <line x1="620" y1="80" x2="450" y2="80" stroke="#7f8c8d" stroke-width="2"/>
                    
                    <!-- リクエスト/レスポンス -->
                    <text x="250" y="65" text-anchor="middle" font-size="10" fill="#7f8c8d">リクエスト→</text>
                    <text x="250" y="95" text-anchor="middle" font-size="10" fill="#7f8c8d">←レスポンス</text>
                </g>
            </svg>
        </div>
        
        <div class="explanation">
            <strong>サーバーの特徴：</strong>
            <ul>
                <li><strong>サービス提供者：</strong>クライアントからの要求に応答</li>
                <li><strong>高可用性：</strong>停止すると多くのユーザーに影響</li>
                <li><strong>リモート管理：</strong>SSH等でネットワーク経由で操作</li>
                <li><strong>専用OS：</strong>Linux、Windows Server等のサーバー向けOS</li>
            </ul>
        </div>
        
        <div class="key-point">
            <strong>重要：</strong>サーバーは特別な形のコンピュータだけを指すのではなく、「役割」を表す言葉です。通常のPCでも、サーバーソフトウェアを動かしてサービスを提供すれば、そのPCはサーバーとして振る舞います。
        </div>
        
        <h2>0.4 まとめ</h2>
        
        <div class="explanation">
            <ul>
                <li>PCはCPU（計算）・メモリ（作業）・ストレージ（保存）が連携して動く</li>
                <li>OSはアプリがハードウェアを直接操作しなくて済むようにする</li>
                <li>サーバーは「サービスを提供する役割」を持ったコンピュータであり、停止しづらい・リモートで管理することが多い</li>
            </ul>
        </div>
        
        <div class="key-point">
            <strong>次章予告：</strong>次章では、Linuxを操作するための「必須コマンド」をまとめて学びます。
        </div>
</div>
