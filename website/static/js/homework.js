let url = $("#url")[0].innerHTML;
let token = $("#token")[0].innerHTML;

$("#homeworkForm").submit(formSubmit);

function formSubmit(e) {
  raw_data = $("#homeworkForm").serializeArray();
  if (
    raw_data.every(function (field) {
      return field.value != "";
    })
  ) {
    finished = $("#finishedCheckbox")[0].checked;
    data = {
      subject: raw_data[0].value,
      name: raw_data[1].value,
      description: raw_data[2].value,
      due_date: raw_data[3].value,
      finished: finished,
    };
    $.ajax({
      url: url,
      type: "POST",
      headers: { Authorization: `Token ${token}` },
      data: JSON.stringify(data),
      success: success,
      error: error,
      contentType: "application/json",
      dataType: "json",
    });
  }
}

function success(result, status, xhr) {
  function p(i) { // padd time
    return i < 10 ? "0" + i : i;
  }
  date = new Date(result.due_date);
  dateStr = `${date.getFullYear()}-${p(date.getMonth())}-${p(date.getDate())} ${p(date.getHours())}:${p(date.getMinutes())}`;
  tr = document.createElement("tr");
  tr.innerHTML = `
          <td>${result.subject}</td>
          <td>${result.name}</td>
          <td>${result.description}</td>
          <td>${dateStr}</td>
          <td class="text-center">
            <div class="checkbox">
              <label> <input type="checkbox" value="finished" ${result.finished ? "checked" : ""} /> </label>
            </div>
          </td>`;
  $("#homeworkTable")[0].append(tr);
  alert("Homework added");
}

function error(xhr, status, error) {
  console.log(xhr);
  console.log(status);
  console.log(error);
}
