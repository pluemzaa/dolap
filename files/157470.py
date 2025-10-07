<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab2.3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 08:19:06 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtUUwxSzI1TEk7MjU2OC0wNy0xNzswMzowMzo1MiBQTTsyNzUw"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtUUwxSzI1TEk7MjU2OC0wNy0yMjswODoxOTowNiBQTTsxMDsyOTEz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="y, years, interest, m" type="Integer" array="False" size=""/>
            <declare name="inter, s, round" type="Real" array="False" size=""/>
            <assign variable="y" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="y &lt; years">
                <assign variable="s" expression="1+(interest/100)"/>
                <assign variable="inter" expression="m*s"/>
                <assign variable="m" expression="inter"/>
                <output expression="&quot;Years&quot; &amp;(y+1)&amp; &quot;:&quot; &amp;inter" newline="True"/>
                <assign variable="y" expression="y+1"/>
            </while>
        </body>
    </function>
</flowgorithm>