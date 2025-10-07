<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 09:10:26 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtUlFSMlJOTDY7MjU2OC0wNy0xNzswODozNTo0MCBBTTsyNzk0"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtUlFSMlJOTDY7MjU2OC0wNy0xNzswOToxMDoyNiBBTTsxMzsyOTUx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i &lt; years">
                <assign variable="i" expression="i + 1"/>
                <assign variable="money" expression="money * (1 + interest/100)"/>
                <output expression="&quot;Year&quot; &amp;i&amp; &quot;:&quot; &amp;money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>