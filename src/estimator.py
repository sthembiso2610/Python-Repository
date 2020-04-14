def estimator(data):
  input = data
  impact.currentlyInfected = input.reportedCases * 10
  severeImpact.currentlyInfected = input.reportedCases * 50 
  return data 
