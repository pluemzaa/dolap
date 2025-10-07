<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab 4"/>
        <attribute name="authors" value="DELL"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 06:15:56 PM"/>
        <attribute name="created" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNjowOTozMiBQTTsyNjYx"/>
        <attribute name="edited" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNzo0ODoxMyBQTTsxO0RFTEw7REVTS1RPUC1ISkcwTE1NOzI1NjgtMDctMjA7MDY6MDk6MzIgUE07NTQ5Mg=="/>
        <attribute name="edited" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMTswNjoxNTo1NiBQTTs1OzI3Nzc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="years, i, n" type="Integer" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <assign variable="n" expression="3"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i&lt;=n">
                <assign variable="money" expression="(1+interest/100)*money"/>
                <output expression="&quot;Year&quot;  &amp; i &amp; &quot; :&quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>