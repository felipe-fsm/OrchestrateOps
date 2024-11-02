{{/*
Função auxiliar para gerar o nome base do Chart
*/}}
{{- define "orchestrateops.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{/*
Função auxiliar para gerar o nome completo do release
*/}}
{{- define "orchestrateops.fullname" -}}
{{- printf "%s-%s" .Release.Name (include "orchestrateops.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end }}
