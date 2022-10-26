let emissionObject = {
    '4P10_96kW' : ['JP09','JP17'],
    '4P10_129kW': ['JP17'],
    '4P10_110kW' : ['JP17'],
    '4P10_96kW' : ['JP17'],
    '4P10_81kW' : ['JP17'],
}

let axleObject = {
    'D035H': ['4x2', '4x4'], 
    'D050HT': ['8x4'], 
    'D040H': ['4x2'],
    'D033H': ['4x2', '4x4'], 
    'D033H D3H(4WD)': ['4x2', '4x4'], 
    'D3H': ['4x2', '4x4']
}

let axleRatioObject = {
    'D035H 4x2': ['5.714'], 
    'D050HT 8x4': ['5.714'], 
    'D040H 4x2': ['4.875'], 
    'D033H 4x2': ['3.545', '3.727', '3.9', '4.111', '4.444', '4.875', '5.285'], 
    'D033H D3H(4WD) 4x2': ['4.111', '4.444'],
    'D3H 4x2': ['4.111', '4.444'],
    'D033H 4x4': ['4.111', '4.444'],
    'D033H D3H(4WD) 4x4': ['4.111', '4.444'],
    'D035H 4x4': ['4.875', '5.285', '5.714', '6.166'],
    'D3H 4x4': ['4.111']
}

let axelefficiencyObject = {
    'D035H 4x2 5.714': ['0.95'],
    'D050HT 8x4 5.714': ['0.93'],
    'D040H 4x2 4.875': ['0.95'],
    'D033H 4x2 3.545': ['0.95'],
    'D033H 4x2 3.727': ['0.95'],
    'D033H 4x2 3.9': ['0.95'],
    'D033H 4x2 4.111': ['0.95'], 
    'D033H 4x2 4.444': ['0.95'], 
    'D033H 4x2 4.875': ['0.95'], 
    'D033H 4x2 5.285': ['0.95'], 
    'D033H D3H(4WD) 4x2 4.111': ['0.95'],
    'D033H D3H(4WD) 4x2 4.444': ['0.95'], 
    'D3H 4x2 4.111': ['0.95'], 
    'D3H 4x2 4.444': ['0.95'], 
    'D033H 4x4 4.111': ['0.93'], 
    'D033H 4x4 4.444': ['0.95'], 
    'D033H D3H(4WD) 4x4 4.111': ['0.95'], 
    'D033H D3H(4WD) 4x4 4.444': ['0.95'], 
    'D035H 4x4 4.875': ['0.95'], 
    'D035H 4x4 5.285': ['0.95'], 
    'D035H 4x4 5.714': ['0.95'], 
    'D035H 4x4 6.166': ['0.95'], 
    'D3H 4x4 4.111': ['0.95']
}

let tyreapplicationObject = {

}

let tyreradiusObject = {
    '195/75R15': ['327'], 
    '265/60 R 22.5': ['437'], 
    '185/85R16': ['350'], 
    '195/85R15': ['346'], 
    '195/85R16': ['358'], 
    '205/70R16': ['338'], 
    '205/70R17.5': ['358'], 
    '205/75R16': ['347'], 
    '205/85R16': ['366'], 
    '225/80R17.5': ['389']}

let tyrerratioObject = {
    '195/75R15 327': ['0.0063'], 
    '265/60 R 22.5 437': ['0.0063'], 
    '185/85R16 350': ['0.0063'], 
    '195/85R15 346': ['0.0063'], 
    '195/85R16 358': ['0.0063'], 
    '205/70R16 338': ['0.0063'], 
    '205/70R17.5 358': ['0.0063'], 
    '205/75R16 347': ['0.0063'], 
    '205/85R16 366': ['0.0063'], 
    '225/80R17.5 389': ['0.0063']}

function filteremission() {
    $("#emission_type").empty();
    $("#emission_type").append("<option value='' selected disabled>Select</option>");
    emissionObject[$("#engine_type").val()].forEach(value =>{
        let optionTemplate = `<option value="${value}" >${value}</option>`
        $("#emission_type").append(optionTemplate);
    });

}

function filterAxleLayout() {
    $("#axle_layout_type").empty();
    $("#axle_layout_type").append("<option value='' selected disabled>Select</option>");

    $("#ratio_type").empty();
    $("#ratio_type").append("<option value='' selected disabled>Select</option>");
    
    $("#efficiency_type").empty();
    $("#efficiency_type").append("<option value='' selected disabled>Select</option>");
    axleObject[$("#axel_type").val()].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`
        $("#axle_layout_type").append(optionTemplate);
    });
}

function filterRatio() {
    $("#ratio_type").empty();
    $("#ratio_type").append("<option value='' selected disabled>Select</option>");

    $("#efficiency_type").empty();
    $("#efficiency_type").append("<option value='' selected disabled>Select</option>");

    let axle_ratio_string = `${$("#axel_type").val()} ${$("#axle_layout_type").val()}`
    axleRatioObject[axle_ratio_string].forEach(value => {
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#ratio_type").append(optionTemplate);
    });
}

function filterEfficiency(){
    $("#efficiency_type").empty();
    $("#efficiency_type").append("<option value='' selected disabled>Select</option>");
    let axle_efficiency_string = `${$('#axel_type').val()} ${$("#axle_layout_type").val()} ${$("#ratio_type").val()}`
    axelefficiencyObject[axle_efficiency_string].forEach(value => {
        let optionTemplate = `<option value="${value}">${value}</option>`;
        $("#efficiency_type").append(optionTemplate);
    });
}

function filterradius(){
    $("#radius_type").empty();
    $("#radius_type").append("<option value='' selected disabled>Select</option>");

    $("#rrc_type").empty();
    $("#rrc_type").append("<option value='' selected disabled>Select</option>");
    tyreradiusObject[$("#tyre_type").val()].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#radius_type").append(optionTemplate);
    });
    $("#Tyre_details").show();
    if ($("#tyre_type").val() === "195/75R15"){
        $("#pattern").val("327")
        $("#std").val("JATMA")
        $("#remark").val("BS ")
    }else if($("#tyre_type").val() === "265/60 R 22.5"){
        $("#pattern").val("Lib")
        $("#std").val("ETRTO")
        $("#remark").val("TOYO 123")
    }else if($("#tyre_type").val() === "185/85R16"){
        $("#pattern").val("350")
        $("#std").val("JATMA")
        $("#remark").val("Yokohama")
    }else if($("#tyre_type").val() === "195/85R15"){
        $("#pattern").val("346")
        $("#std").val("JATMA")
        $("#remark").val("BS")
    }else if($("#tyre_type").val() === "195/85R16"){
        $("#pattern").val("358")
        $("#std").val("JATMA")
        $("#remark").val("Yokohama")
    }else if($("#tyre_type").val() === "205/70R16"){
        $("#pattern").val("338")
        $("#std").val("JATMA")
        $("#remark").val("Yokohama")
    }else if($("#tyre_type").val() === "205/70R17.5"){
        $("#pattern").val("358")
        $("#std").val("JATMA")
        $("#remark").val("BS")
    }else if($("#tyre_type").val() === "205/75R16"){
        $("#pattern").val("347")
        $("#std").val("JATMA")
        $("#remark").val("MS")
    }else if($("#tyre_type").val() === "205/85R16"){
        $("#pattern").val("366")
        $("#std").val("JATMA")
        $("#remark").val("MS")
    }else{
        $("#pattern").val("389")
        $("#std").val("JATMA")
        $("#remark").val("MS")
    };

}

function filterrrc(){
    $("#rrc_type").empty();
    $("#rrc_type").append("<option value='' selected disabled>Select</option>");
    let rrc_string = `${$("#tyre_type").val()} ${$("#radius_type").val()}`
    tyrerratioObject[rrc_string].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#rrc_type").append(optionTemplate);
    });
   

}

function loading(){
    let all_input = []
    let input = document.querySelectorAll("input");
    let select = document.querySelectorAll("select");
    input.forEach(function(i){
        all_input.push(i.value);
    })
    select.forEach(function(i){
        all_input.push(i.value);
    })
    
    if (all_input.includes('') ){
        $("#content").show()
        
    }
    else{
        $("#loading").show()
        // $("#content").show()
        
    };
}

function getgearno(value){
    $("#Geardiv").show()
    if($("#transmission_type").val() === value[0]){
        $("#gear_display").val("6")}
    else if($("#transmission_type").val() === value[1]){
        $("#gear_display").val("5")}
    else{
        $("#gear_display").val("12")
    }
  
  }

function uppercase(){
        var x = document.getElementById("Torque_cut");
        x.value = x.value.toUpperCase();
      
}


function output_mesage(){
    $("#result").show()
}

function page_load() {
    window.location.href = "http://127.0.0.1:5050/";
  }


// if (document.querySelectorAll("input").forEach(input => input.value !== "") && document.querySelectorAll("select").forEach(input => input.value !== "")){
// // document.querySelectorAll("input").forEach(input => flag =  input.value !== "");

