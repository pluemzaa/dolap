<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="MY PC JO E"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 01:19:33 AM"/>
        <attribute name="created" value="TVkgUEMgSk8gRTtTTFVQUElFWEJBUlpFRDsyNTY4LTA3LTE5OzA1OjEzOjU3IFBNOzMwMDg="/>
        <attribute name="edited" value="TVkgUEMgSk8gRTtTTFVQUElFWEJBUlpFRDsyNTY4LTA3LTE5OzA2OjI5OjIyIFBNOzY7MzEyMQ=="/>
        <attribute name="edited" value="VXNlcjtKRVM7MjU2OC0wNy0yMTswMToxOTozMyBBTTsxOzIwMjY="/>
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
            <while expression="year &gt;= i">
                <assign variable="money" expression="money*(1 + interest/100)"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>