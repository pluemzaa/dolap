<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="myself_3"/>
        <attribute name="authors" value="ateru"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 09:33:10 PM"/>
        <attribute name="created" value="YXRlcnU7VEhBTlBJVENIQTsyMDI1LTA3LTIwOzA5OjIwOjA0IFBNOzI1NjI="/>
        <attribute name="edited" value="YXRlcnU7VEhBTlBJVENIQTsyMDI1LTA3LTIwOzA5OjMzOjEwIFBNOzE7MjY3MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="e, s" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="e"/>
            <while expression="s&lt;=e">
                <output expression="s" newline="True"/>
                <assign variable="s" expression="s+1"/>
            </while>
        </body>
    </function>
</flowgorithm>