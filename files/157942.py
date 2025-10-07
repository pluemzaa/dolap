<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="683380460-1_2"/>
        <attribute name="authors" value="acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 04:36:14 PM"/>
        <attribute name="created" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0yMTswMTo1OTo1MyBQTTsyNzQz"/>
        <attribute name="edited" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0yMTswNDozNjoxNCBQTTszOzI4NDg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startnumber, endnumber, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="startnumber"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="endnumber"/>
            <assign variable="i" expression="startnumber"/>
            <while expression="i &lt;= endnumber">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>