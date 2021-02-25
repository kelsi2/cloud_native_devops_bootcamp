# To run the test:
# Invoke-Pester ./New-ResourceGroup_test.ps1

Describe "New-ResourceGroup" {
  
  It "Name should be cloudskillsbootcamp" {
    $name = 'cloudskillsbootcamp'
    $name | Should -Be 'cloudskillsbootcamp'
  }
  
  It "location should be westus2" {
    $location = 'westus2'
    $location | Should -Be 'westus2'
  }
}