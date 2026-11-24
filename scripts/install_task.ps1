# Registers a Windows Task Scheduler task that relaunches `python -m harness run`
# at logon and every 30 minutes. The harness's lock file (state\harness.lock) makes sure only one copy runs;
# extra launches print "already running" and exit straight away.
#
# Install:    powershell -ExecutionPolicy Bypass -File scripts\install_task.ps1
# Remove:     powershell -ExecutionPolicy Bypass -File scripts\install_task.ps1 -Remove
param([switch]$Remove)

$TaskName = "G2G-Eval-Harness"
$Project  = Split-Path -Parent $PSScriptRoot

if ($Remove) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Output "Removed task $TaskName"
    return
}

# pythonw runs without a console window; output goes to state\harness.out.log
$Pythonw = (Get-Command pythonw.exe -ErrorAction Stop).Source
$Cmd = "/c cd /d `"$Project`" && `"$Pythonw`" -m harness run >> state\harness.out.log 2>&1"

$Action   = New-ScheduledTaskAction -Execute "cmd.exe" -Argument $Cmd -WorkingDirectory $Project
$AtLogon  = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$Every30  = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 30)
$Settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable `
            -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Days 30)

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger @($AtLogon, $Every30) -Settings $Settings `
    -Description "Good-to-great skill eval harness (resumes from state\ledger.db)" -Force | Out-Null
Write-Output "Registered task $TaskName (at logon + every 30 min). Lock file prevents duplicates."
