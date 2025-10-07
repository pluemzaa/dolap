<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 09:05:37 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtMjg4M0RVVU07MjU2OC0wNy0yMDswODo1NzoyNiBQTTsyNzU0"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtMjg4M0RVVU07MjU2OC0wNy0yMDswOTowNTozNyBQTTsxOzI4NTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i, year1, year2, year3, total" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="total" expression="money"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=years">
                <assign variable="total" expression="total*(1+interest/100)"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;:&quot;&amp;total" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>