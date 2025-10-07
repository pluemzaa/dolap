<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flowchart.lap4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 03:00:08 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtQVNBRkZPNlY7MjAyNS0wNy0yMTswMjo1Mzo1NiBQTTsyNzgw"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQVNBRkZPNlY7MjAyNS0wNy0yMTswMzowMDowOCBQTTsxOzI4Nzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <while expression="year&gt;=i">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;:&quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>