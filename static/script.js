function func()
{
    document.getElementById('signup2').style.transform='translateX(-100%)';
    document.getElementById('signin2').style.transform='translateX(0)';
    document.getElementById('signup2').style.visibility='hidden';
    document.getElementById('signin1').style.visibility='hidden';
    document.getElementById('signup1').style.visibility='visible';
    document.getElementById('signin2').style.visibility='visible';

    document.getElementById('alert1').style.visibility='hidden';
    
}

function func1()
{
    document.getElementById('signup2').style.transform='translateX(0)';
    document.getElementById('signin2').style.transform='translateX(100%)';
    document.getElementById('signup2').style.visibility='visible';
    document.getElementById('signin1').style.visibility='visible';
    document.getElementById('signup1').style.visibility='hidden';
    document.getElementById('signin2').style.visibility='hidden';

    document.getElementById('alert1').style.visibility='hidden';

}

function message_hide()
{
    document.getElementById('alert1').style.display='none';
}

