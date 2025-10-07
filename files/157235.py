<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab.4.4"/>
        <attribute name="authors" value="ADVICE"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 08:04:26 PM"/>
        <attribute name="created" value="QURWSUNFO0RFU0tUT1AtQVFMRklHODsyMDI1LTA3LTE2OzA4OjAwOjI3IFBNOzI3ODc="/>
        <attribute name="edited" value="QURWSUNFO0RFU0tUT1AtQVFMRklHODsyMDI1LTA3LTIxOzA4OjA0OjI2IFBNOzEzOzI5NDU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, total, year, years" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <assign variable="interest" expression="interest/100"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="total" expression="money"/>
            <assign variable="year" expression="0"/>
            <while expression="year &lt; years">
                <assign variable="total" expression="total*(1+interest)"/>
                <output expression="&quot;Year &quot; &amp;year+1&amp; &quot;: &quot; &amp; total" newline="True"/>
                <assign variable="year" expression="year+1"/>
            </while>
        </body>
    </function>
</flowgorithm>