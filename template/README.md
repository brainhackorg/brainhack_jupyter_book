# template_repo_for_projects_labelling

This repo contains a template that can be used to create a new repo to host issues
for a brainhack event and label its porject issues:

- help tag projects with specific labels

`labels.json` contain a list of labels for issues

To use it:

- go to label page of the repo
- open the browser console
- copy paste the snippet and change the variable `labels_export` with the
  content of `labels.json`
- execute the cellule.

```javascript
labels_export = [
  TODO: Add labels here
]

labels_export.forEach(function(label) {
  addLabel(label)
})

function updateLabel (label) {
  var flag = false;
  [].slice.call(document.querySelectorAll(".js-labels-list-item"))
  .forEach(function(element) {
    if (element.querySelector('.js-label-link').textContent.trim() === label.name) {
      flag = true
      element.querySelector('.js-edit-label').click()
      element.querySelector('.js-new-label-name-input').value = label.name
      element.querySelector('.js-new-label-color-input').value = '#' + label.color
      element.querySelector('.js-new-label-description-input').value = label.description
      element.querySelector('.js-edit-label-cancel ~ .btn-primary').disabled = false
      element.querySelector('.js-edit-label-cancel ~ .btn-primary').click()
    }
  })
  return flag
}

function addNewLabel (label) {
  document.querySelector('.js-new-label-name-input').value = label.name
  document.querySelector('.js-new-label-color-input').value = '#' + label.color
  document.querySelector('.js-new-label-description-input').value = label.description
  document.querySelector('.js-details-target ~ .btn-primary').disabled = false
  document.querySelector('.js-details-target ~ .btn-primary').click()
}

function addLabel (label) {
  if (!updateLabel(label)) addNewLabel(label)
}
```
