SELECT -- The width of the frame e.g the columns included
invoice.month as invoiceMonth,
billing_account_id,
sum(cost) as cost,
service.id as serviceId
service.description as serviceDescription,
sku.description as sku,
resource.name as resourceName,
project.id as projectId,
project.name as projectName,
TO_JSON_STRING(project.labels) as labelsid, -- project.labels.key / project.labels.value
currency,
location.location as region,
usage.unit as usageUnit,
sum(usage.amount) as usageAmount,
cost_type
cast(usage_start_time as date) as startdate,
cast(usage_end_time as date) as enddate

FROM '@projectName.@datasetName.@tableName'
WHERE billing_account_id = '@billing_account_id' -- The length of the frame e.g the rows included
AND invoice.month BETWEEN '@yyyyMM' AND '@yyyyMM'
AND cast(usage_start_time as date) >= date_add(CURRENT_DATE(),INTERVAL -90 DAY)
AND usage.amount > 0
GROUP BY startdate, enddate, billing_account_id, cost_type, serviceId, region, usageUnit, projectName, projectId,currency, invoiceMonth, serviceDescription, sku, resourceName, labelsid

