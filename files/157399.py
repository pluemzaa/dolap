<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="aaaaaaaainterrest"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 11:53:36 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xODsxMTo0NToyOSBBTTsyNzcx"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xODsxMTo1MzozNiBBTTsxOzI4NzY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="fmoney, fyear, lyear, interest" type="Real" array="False" size=""/>
            <assign variable="fyear" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="fmoney"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="lyear"/>
            <while expression="fyear&lt;lyear">
                <assign variable="fyear" expression="fyear+1"/>
                <assign variable="fmoney" expression="fmoney*(1+(interest/100))"/>
                <output expression="&quot;Year&quot;&amp;fyear&amp;&quot;:&quot;&amp;fmoney" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>